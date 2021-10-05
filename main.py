from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/hello')
def hello():
    return "hello hello kitty"

@app.route('/lyn')
def lyn():
    return "Hi, my name is lyn"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
