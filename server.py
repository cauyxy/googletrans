import flask
from flask import request

server = flask.Flask(__name__)

@server.route('/', methods=['get'])
def api():
    str = request.values.get('parameter')

    return str+"Aliyun"

if __name__ == '__main__':

    server.run(debug=True, port=8888,host="0.0.0.0")
