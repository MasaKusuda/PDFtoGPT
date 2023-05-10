from flask import Flask, render_template, request, jsonify,send_from_directory
from flask_bootstrap import Bootstrap
from src import api_test
import os
app = Flask(__name__)
app.debug = False
app.config["UPLOAD_FOLDER"] = "./uploads"
Bootstrap(app)
messages=[]
token_sum=0
token_MAX=4096

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "pdf" not in request.files:
            return "No file part"

        file = request.files["pdf"]
        if file.filename == "":
            return "No selected file"

        if file:
            filename = "uploaded_pdf.pdf"
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            pdf_text = api_test.read_pdf_to_text(filepath)
            messages.append({"role":"user","content":pdf_text})
            return render_template("index.html", filename=filename,pdf_text=pdf_text)

    return render_template("index.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route('/process', methods=['POST'])
def process():
    input_text = request.form['input_text']
    # ここで input_text を使用してPythonコードを実行できます。
    print(input_text)
    messages.append({"role":"user","content":input_text})
    res = api_test.access_to_GPT(messages)
    res_role = res["choices"][0]["message"]["role"]
    res_content = res["choices"][0]["message"]["content"]
    messages.append({"role":res_role,"content":res_content})
    response_text = res_content
    token_sum = token_sum + int(res["usage"]["total_tokens"])
    token_used_percentage = int((token_sum / token_MAX)*100) 
    response={
        "response_text":response_text,
        "token_sum":token_sum,
        "token_used_percentage":token_used_percentage
    }
    return jsonify(response)


# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run(host='0.0.0.0', port=8000)