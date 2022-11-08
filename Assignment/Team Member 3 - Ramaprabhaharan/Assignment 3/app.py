from flask import Flask,render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route("/")
def log():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)