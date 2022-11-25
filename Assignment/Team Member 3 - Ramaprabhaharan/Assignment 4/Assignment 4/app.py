from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1 style='text-align:center;color:red'>Skill and job recommender</h1> <br><br><h3>Hello, World!</h3><br><br><br><footer style='text-align:center;color:Blue'> This app is devoloped By-<br> Pasupathy G <br>Arul M<br>Gopinath B <br> Ramaprabhakaran R </footer>"

if __name__ == "__main__":
    app.run(debug=True)