#!/usr/bin/env python3
from markupsafe import escape
from flask import Flask

app = Flask("hello")

@app.route("/")
def index():
    return "Hello world"

@app.route("/<name>")
def hello(name):
    return f"<p>hello {escape(name)}</p>"
