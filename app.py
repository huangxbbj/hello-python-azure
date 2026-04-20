from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Azure CI/CD 🚀 Version 6"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
