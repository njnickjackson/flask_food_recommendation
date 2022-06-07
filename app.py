import os

from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home_page.html")


@app.route('/HelpMeChoose')
def choose():
    return render_template("help_choose.html")


if __name__ == '__main__':
    app.run()
