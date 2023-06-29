import unittest
from unittest.mock import MagicMock, patch
from flask import Flask, json
from global_routes import app, extract_responses, positive_feedback, negative_feedback
from global_service import GlobalService
from global_dao import GlobalDAO

class TestGlobalRoutes(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.add_url_rule('/global-api/keyword-hits', 'extract_responses', extract_responses, methods=['GET'])
        self.app.add_url_rule('/global-api/positive-feedback', 'positive_feedback', positive_feedback, methods=['GET'])
        self.app.add_url_rule('/global-api/negative-feedback', 'negative_feedback', negative_feedback, methods=['GET'])
        self.client = self.app.test_client()
    
    @patch.object(GlobalDAO, 'connect_to_database')
    @patch.object(GlobalDAO, 'extract_responses')
    def test_extract_responses_endpoint(self, mock_extract_responses, mock_connect_to_database):
        # Prepare test data
        mock_result = [
            {
                'id': 1,
                'keyword_hits': 2,
                'response': 'Response 1'
            },
            {
                'id': 2,
                'keyword_hits': 1,
                'response': 'Response 2'
            }
        ]
        mock_extract_responses.return_value = mock_result
        mock_connect_to_database.return_value = MagicMock()

        # Send a GET request to the endpoint
        response = self.client.get('/global-api/keyword-hits', json={'keywords': 'keyword1,keyword2'})

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_result)
        mock_extract_responses.assert_called_once_with('keyword1,keyword2')

    @patch.object(GlobalDAO, 'connect_to_database')
    @patch.object(GlobalDAO, 'update_positive_feedback')
    def test_positive_feedback_endpoint(self, mock_update_positive_feedback, mock_connect_to_database):
        # Prepare test data
        mock_result = [
            {
                'id': 1,
                'probability': 0.5
            },
            {
                'id': 2,
                'probability': 0.6
            }
        ]
        mock_update_positive_feedback.return_value = mock_result
        mock_connect_to_database.return_value = MagicMock() 

        # Send a get request to the endpoint
        response = self.client.get('/global-api/positive-feedback', json={"id": "1,2"})

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_result)
        mock_update_positive_feedback.assert_called_once_with("1,2", 0.1)

    @patch.object(GlobalDAO, 'connect_to_database')
    @patch.object(GlobalDAO, 'update_negative_feedback')
    def test_negative_feedback_endpoint(self, mock_update_negative_feedback, mock_connect_to_database):
        # Prepare test data
        mock_result = [
            {
                'id': 1,
                'probability': 0.4
            },
            {
                'id': 2,
                'probability': 0.3
            }
        ]
        mock_update_negative_feedback.return_value = mock_result
        mock_connect_to_database.return_value = MagicMock() 

        # Send a get request to the endpoint
        response = self.client.get('/global-api/negative-feedback', json={"id": "1,2"})

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_result)
        mock_update_negative_feedback.assert_called_once_with("1,2", 0.1)

if __name__ == '__main__':
    unittest.main()
