from flask import Flask, request, jsonify
from bond_service import BondService
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.secret_key = 'secret'
bond_service = BondService()

@app.route('/')
def home():
    return 'Server running.'

@app.route('/bonds-api', methods=['POST'])
def bonds_api():
    return bond_service.process_bond_api_request()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='9000')
