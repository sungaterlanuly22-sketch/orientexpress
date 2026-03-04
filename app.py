import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "secret123"

# 🔹 НАСТРОЙКИ Gmail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'orienttexpresss@gmail.com'
app.config['MAIL_PASSWORD'] = 'APP_PASSWORD'
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

# Главная
@app.route("/")
def home():
    return render_template("index.html")


# 🔽 ВСТАВИТЬ СЮДА
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

# Контакты + отправка письма
@app.route("/contact")
def contact():
    return render_template("contact.html")
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        msg = Message(
            subject="Новая заявка с сайта",
            sender=app.config["MAIL_USERNAME"],
            recipients=["orienttexpresss@gmail.com"]
        )

        msg.html = f"""
        <h3>Новое сообщение сайта</h3>
        <p><b>Имя:</b> {name}</p>
        <p><b>Email:</b> {email}</p>
        <p><b>Сообщение:</b><br>{message}</p>
        """

        try:
            mail.send(msg)
            flash("Сообщение отправлено!")
        except Exception as e:
            print("ОШИБКА ПОЧТЫ:", e)
            flash("Ошибка отправки сообщения. Почта временно не работает.")

        return redirect(url_for("contact"))

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)