from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "hello world"

@app.route('/hello')
def index():
    return "hello hello"

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
