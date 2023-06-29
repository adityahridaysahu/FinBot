import unittest
from unittest.mock import patch, MagicMock
from flask import Flask, json
from central_routes import get_feedback, return_answer, central_service, feedback_service
from central_dao import ConvoDAO, GlobalDAO
from json import JSONEncoder, dumps

class TestCentralRoutes(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = False

        # Add URL rules before the first request is handled
        self.app.add_url_rule('/', 'central_resource', return_answer, methods=['POST'])
        self.app.add_url_rule('/feedback', 'feedback_resource', get_feedback, methods=['POST'])

        central_service.convo_dao = MagicMock(spec=ConvoDAO)
        central_service.global_dao = MagicMock(spec=GlobalDAO)

        feedback_service.convo_dao = MagicMock(spec=ConvoDAO)
        feedback_service.global_dao = MagicMock(spec=GlobalDAO)

        self.client = self.app.test_client()


    @patch.object(ConvoDAO, 'mask_session')
    def test_central_resource_endpoint(self, mock_mask_session):
        # Prepare test data
        mock_result = {
            "unique_id": "1103ba0a-42",
            "cum_sum_user": "Cumulative summary user",
            "cum_sum_bot": "Cumulative summary bot"
        }
        mock_mask_session.return_value = mock_result

        # Send a POST request to the endpoint
        response = self.client.post('/', json={
            'query': 'What are the types of bonds in the financial market?',
            'session_id': '1103ba0a-42'
        })

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['session_id'], mock_result['unique_id'])
        self.assertEqual(response.json['status'], "working")


    @patch.object(GlobalDAO, 'get_feedback')
    @patch.object(ConvoDAO, 'mask_session')
    def test_feedback_resource_endpoint(self, mock_mask_session, mock_get_feedback):
        # Prepare test data
        mock_session_result = {
            "unique_id": "1103ba0a-42",
            "global_hits": "1,2"
        }
        mock_feedback_result = {
            "updated": True
        }
        mock_get_feedback.return_value = mock_feedback_result
        mock_mask_session.return_value = mock_session_result

        response = self.client.post('/feedback', json={
            'session_id': '1103ba0a-42',
            'timeout': False,
            'clicked': True
        })

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['updated'], mock_feedback_result['updated'])


if __name__ == '__main__':
    unittest.main()
