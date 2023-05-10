from flask import Flask, render_template, request, url_for,send_from_directory
from flask_bootstrap import Bootstrap
from src import api_test
import os
app = Flask(__name__)
app.debug = True


# http://127.0.0.1:5000をルートとして、("")の中でアクセスポイント指定
# @app.route("hoge")などで指定すると、http://127.0.0.1:5000/hogeでの動作を記述できる。
app.config["UPLOAD_FOLDER"] = "./uploads"
Bootstrap(app)

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
            return render_template("index.html", filename=filename,pdf_text=pdf_text)

    return render_template("index.html")

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

@app.route('/form')
def form(name=None):
   return render_template('form.html',name=name)


@app.route('/hello')
def hello_render(name = None):
    return render_template('hello.html',name=name)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run(host='0.0.0.0', port=5000)