import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>You did it!</h1><img src=\"img/logo.png\" height=458 width=600 />"

if __name__ == "__main__":
    app.run(host='0.0.0.0', static_files={
            '/img': os.path.join(os.path.dirname(__file__), 'img')
        })
