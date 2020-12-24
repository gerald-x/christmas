from flask import render_template, request, redirect, url_for

from app import app

import random

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        name = request.form.get("name").lower()
        print(name)
        task = []

        with open('messages.txt', 'r', encoding='utf-8') as file:
            for line in file:
                task.append(line.rstrip('\n'))

        message = random.choice(task)
        print(message)
        return render_template("message.html", name=name.capitalize(), message=message)