from flask import Flask
from flask import  jsonify
from flask import request
import random

from model import predict
app = Flask(__name__)

print('started')
@app.route('/')
def hello_world():
    print(1)
    return 'Hello, World!'


@app.route('/get_prob/url',methods=['GET', 'POST'])
def get_prob_url():
    url=request.args.get('url')
    app.logger.debug(url)
    return jsonify(
        {

            "url":url,
            "prob": predict(request.args.get('url'))[0][0]
        }
    ), 200

@app.route('/get_prob/text',methods=['GET', 'POST'])
def get_prob_text():
    return jsonify(
        {
            "text":request.args.get('text'),
            "prob": random.random()
        }
    ), 200



@app.route('/get_prob/url/<url>')
def get_prob_url1(url):
    return jsonify(
        {
            "url":url,
            "prob": predict(url)[0][0]
        }
    ), 200

@app.route('/get_prob/text/<text>')
def get_prob_text1(text):
    return jsonify(
        {
            "text":text,
            "prob": random.random()
        }
    ), 200

if __name__ == "__main__":
    app.run(port='8080', host='0.0.0.0')