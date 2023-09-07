from flask import Flask, render_template, request
import socket

app = Flask(__name__)

def is_running(site):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((site, 80))
        return True
    except:
        return False

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        site = request.form["site"]
        if is_running(f"{site}.com"):
            result = f"{site}.com is running!"
        else:
            result = f"There is a problem with {site}.com!"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
