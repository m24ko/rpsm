from flask import Flask

app = Flask(__name__)


@app.route("/kitica")
def hello():
    return "Hello World!"
