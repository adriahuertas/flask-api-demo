from flask import Flask

app = Flask(__name__)


# Home route to check it's working
@app.route("/")
def home():
    return "Hello World"

