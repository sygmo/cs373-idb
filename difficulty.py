from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)

@app.route("/")
def difficulty() :
    return "Hello World!"

if __name__ == "__main__" :
    app.run()