from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/joinus")
def joinus():
    return render_template("joinus.html")

@app.route("/signin")
def signin():
    return "signin"

@app.route("/signup")
def signup():
    return "signup"

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)