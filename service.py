from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():
    return "root"

@app.route("/endpoint1/", methods=['GET'])
def endpoint1():
    return "endpoint1"

@app.route("/sunnyis/", methods=['GET'])
def sunny():
    return "not fat"


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5005)