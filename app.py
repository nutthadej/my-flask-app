from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "สวัสดีครับพี่เอ็มต่ะ! เว็บนี้รันบน Render 🚀"
