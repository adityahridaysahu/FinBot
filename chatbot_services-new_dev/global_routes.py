from flask import Flask, jsonify, request
from global_service import GlobalService
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.secret_key = 'secret'
global_service = GlobalService()

@app.route('/')
def home():
    return 'Server running.'

@app.route('/global-api/keyword-hits')
def extract_responses():
    return jsonify(global_service.extract_responses())

@app.route('/global-api/positive-feedback')
def positive_feedback():
    return jsonify(global_service.positive_feedback())

@app.route('/global-api/negative-feedback')
def negative_feedback():
    return jsonify(global_service.negative_feedback())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='7000')
