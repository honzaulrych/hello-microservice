from flask import Flask

app = Flask(__name__)
import socket

@app.route("/hello/<name>")
def hello(name):
    hostname = socket.gethostname()
    message = f"Hello, {name}! My name is {hostname}."
    response = f'{{\n\t"message": "{message}"\n}}\n'
    code = 200
    return response, code, {'Content-Type': 'application/json'}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5123)