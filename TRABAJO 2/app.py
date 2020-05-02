from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/paginaPrincipal", methods=["GET","POST"])
def paginaPrincipal():
    if request.method == "GET":
        return render_template("paginaError.html")
    name = request.form.get("name")
    return render_template("paginaPrincipal.html", name=name)
