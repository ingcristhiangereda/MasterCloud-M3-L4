from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return f"Hola desde Master UCM - Introducción al CI/CD  2🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)