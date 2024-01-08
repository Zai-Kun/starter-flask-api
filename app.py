from flask import Flask
import re_gpt

app = Flask(__name__)


@app.route("/")
def hello_world():
    return str(re_gpt)
