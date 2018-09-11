from flask import Flask, Response, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def root():
    return "root"

@app.route("/endpoint1/", methods=['GET'])
def endpoint1():
    return "endpoint1"

@app.route("/sunnyis/", methods=['GET'])
def sunny():
    return "obese"

@app.route('/send/', methods=['POST'])
def get_data():
    print('Recieved from client: {}', request.data)
    f = open("data.txt", "w")
    f.write(request.data.decode("utf-8"))
    f.close()
    return Response('We recieved something…')

@app.route("/load/", methods=['GET'])
def send():
    f = open("data.txt", "r")
    data = f.read()
    print(data)
    f.close() 
    return data



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=5000)
