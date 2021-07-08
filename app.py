from flask import Flask, render_template
import datetime
TEMPLATES = "./templates"
STATIC = "./static"

app = Flask(__name__, template_folder=TEMPLATES, static_folder=STATIC)

@app.route("/")
@app.route("/home")
def home():
    nomes = ["Fernando", "Isabelly","José Matheus", "Josiele", "Larah"]
    data = datetime.datetime.now()
    data2 = f"{data:%d/%m/%Y}"
    return render_template("index.html", nomes=nomes, data=data2)
