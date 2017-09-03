from flask import Flask

app = Flask(__name__)


@app.route("/kitica")
def hello():
    x = 5
    y = 4.0
    print x/y
    return "Hello World!"
