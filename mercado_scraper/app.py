from flask import Flask, render_template, request
from scraper import buscar_produtos

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []
    if request.method == "POST":
        termo = request.form.get("termo")
        quantidade = int(request.form.get("quantidade", 10))
        resultados = buscar_produtos(termo, quantidade)
    return render_template("index.html", resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)
