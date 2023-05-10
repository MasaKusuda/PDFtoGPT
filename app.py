from flask import Flask, render_template, request, jsonify,send_from_directory,session
from flask_bootstrap import Bootstrap
from src import api_test
import os
from datetime import timedelta
import openai

openai.api_key_path = "env"
print(openai.Model.list())
app = Flask(__name__)
app.debug = False
app.config["UPLOAD_FOLDER"] = "./uploads"
app.permanent_session_lifetime = timedelta(hours=2)
Bootstrap(app)
#secretkeyは意味のない文字列で代用
app.secret_key = 'gasawrythpoe1235gfd'
# token_sum=0
# token_MAX=4096

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
            session["messages"]=[]
            session["pdf_text"] = api_test.read_pdf_to_text(filepath)
            session["messages"].append({"role":"user","content":session["pdf_text"]})
            session["token_MAX"] = 4096
            return render_template("index.html", filename=filename,pdf_text=session["pdf_text"])

    return render_template("index.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route('/process', methods=['POST'])
def process():
    input_text = request.form['input_text']
    # ここで input_text を使用してPythonコードを実行できます。
    print(input_text)
    session["messages"].append({"role":"user","content":input_text})
    res = api_test.access_to_GPT(session["messages"])
    res_role = res["choices"][0]["message"]["role"]
    res_content = res["choices"][0]["message"]["content"]
    session["messages"].append({"role":res_role,"content":res_content})
    token_used_percentage = int(res["usage"]["total_tokens"] / session["token_MAX"]*100)
    print(token_used_percentage)
    response={
        "response_text":res_content,
        "token_sum":res["usage"]["total_tokens"],
        "token_used_percentage":token_used_percentage
    }
    return jsonify(response)

@app.route('/reset',methods=['POST'])
def reset():
    session["messages"]=[]
    session["messages"].append({"role":"user","content":session["pdf_text"]})
    response={"token_reseted":"true"}
    return jsonify(response)

# @app.route('/upload', methods=['GET', 'POST'])
# def upload_file():
#     if request.method == 'POST':
#         f = request.files['the_file']
#         f.save('/var/www/uploads/uploaded_file.txt')

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run(host='0.0.0.0', port=8000)