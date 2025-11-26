from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates')

latest_message = {"text": "WELCOME - Digital Display BOARD"}  # Initial display text

@app.route("/")
def index():
    return render_template("index.html", current=latest_message["text"])

@app.route("/send", methods=["POST"])
def send():
    message = request.form["message"].strip()
    if message:
        latest_message["text"] = message
        return f"Message sent: {message}"
    return "Empty message", 400

@app.route("/get", methods=["GET"])
def get_msg():
    return jsonify({"msg": latest_message["text"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)