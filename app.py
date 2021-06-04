import flask
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/', methods=['get'])
def home():
    return 'hello world'

if __name__ == "__main__":
    app.run(debug=True)