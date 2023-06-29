from flask import Flask, jsonify, request
from convo_service import ConvoService
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.secret_key = 'secret'
convo_service = ConvoService()

@app.route('/')
def home():
    return 'GOTO: /convo-api/mask-session for creating new session/fetching data from previous session'

@app.route('/convo-api/update-status', methods=['GET', 'POST'])
def update_status():
    return jsonify(convo_service.update_status())

@app.route('/convo-api/mask-session', methods=['GET', 'POST'])
def mask_session():
    return jsonify(convo_service.mask_session())

@app.route('/convo-api/update-summary', methods=['GET', 'POST'])
def update_summary():
    return jsonify(convo_service.update_summary())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
