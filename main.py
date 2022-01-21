from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():

    frase_maiuscula = ''

    if request.method == "GET":
        return render_template("index.html", frase_maiuscula=frase_maiuscula)

    else:
        frase = str(request.form.get("name"))
        frase_maiuscula = frase.upper()
        return render_template("index.html", frase_maiuscula=frase_maiuscula)

app.run(debug=True)