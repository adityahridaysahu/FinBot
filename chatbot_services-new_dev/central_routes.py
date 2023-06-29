from flask import Flask, request, jsonify
from flask_cors import CORS
from central_dao import ConvoDAO, GlobalDAO
from central_service import CentralService, FeedbackService
import json
import nltk

with open("config.json") as config_file:
    config = json.load(config_file)

app = Flask(__name__)
CORS(app)
convo_link = config["convo"]
global_link = config["global"]
bonds_link = config["bonds"]
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
convo_dao = ConvoDAO(convo_link)
global_dao = GlobalDAO(global_link)

central_service = CentralService(convo_dao, global_dao)
feedback_service = FeedbackService(convo_dao, global_dao)

@app.route('/')
def home():
    return 'Server running.'

@app.route('/', methods=['POST'])
def return_answer():
    return jsonify(central_service.process_request())
       

@app.route('/feedback', methods=['POST'])
def get_feedback():
    return jsonify(feedback_service.process_feedback())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="4000")
