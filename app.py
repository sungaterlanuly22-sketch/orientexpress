import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/catalog")
def catalog():
    return render_template("catalog.html")

@app.route("/quality")
def quality():
    return render_template("quality.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# обработка формы
@app.route("/send", methods=["POST"])
def send():

    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    print("Имя:", name)
    print("Email:", email)
    print("Сообщение:", message)

    return redirect("/contact")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))