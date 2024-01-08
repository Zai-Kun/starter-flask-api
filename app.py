from flask import Flask
from datetime import date, datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
