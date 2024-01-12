from flask import Flask
import time
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello_world():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@app.route("/<_idk>")
def idk(_idk):
    time.sleep(15)
    return _idk + "after 15 secs"
