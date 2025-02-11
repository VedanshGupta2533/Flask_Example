from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World this flask</p>"

@app.route("/products")
def products():
    return "<p>This is products page</p>"

if __name__ == "__main__":
    app.run(debug=True)
