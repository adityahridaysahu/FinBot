import unittest
from unittest.mock import MagicMock, patch
from flask import Flask, json
from convo_routes  import update_status, mask_session, update_summary
from convo_dao import ConvoDAO

class TestConvoRoutes(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.add_url_rule('/convo-api/update-status', 'update_status', update_status, methods=['POST'])
        self.app.add_url_rule('/convo-api/mask-session', 'mask_session', mask_session, methods=['POST'])
        self.app.add_url_rule('/convo-api/update-summary', 'update_summary', update_summary, methods=['POST'])
        self.client = self.app.test_client()

    @patch.object(ConvoDAO, 'connect_to_database')
    @patch.object(ConvoDAO, 'update_status')
    def test_update_status_endpoint(self, mock_update_status, mock_connect_to_database):
        # Prepare test data
        mock_result = {
            'unique_ID': '123',
            'isResolved': True,
            'isClosedByUser': False
        }
        mock_update_status.return_value = mock_result
        mock_connect_to_database.return_value = MagicMock() 
        
        # Send a POST request to the endpoint
        response = self.client.post('/convo-api/update-status', json= {
            'unique_ID': '123',
            'isResolved': True,
            'isClosed': False
        })

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_result)
        mock_update_status.assert_called_once_with('123', True, False)

    @patch.object(ConvoDAO, 'mask_session')
    def test_mask_session_endpoint(self, mock_mask_session):
        # Prepare test data
        mock_result = {
            'unique_id': '123',
            'time_stamp': '2023-06-16 12:00:00'
        }
        mock_mask_session.return_value = mock_result

        # Send a POST request to the endpoint
        response = self.client.post('/convo-api/mask-session', json={'unique_ID': '123'})

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_result)
        mock_mask_session.assert_called_once_with('123')

    @patch.object(ConvoDAO, 'update_summary')
    def test_update_summary_endpoint(self, mock_update_summary):
        # Prepare test data
        mock_result = {
            'time_stamp': '2023-06-16 12:00:00',
            'global_hits': ['hit1', 'hit2']
        }
        mock_update_summary.return_value = mock_result

        # Send a POST request to the endpoint
        response = self.client.post('/convo-api/update-summary', json={
            'unique_ID': '123',
            'new_cum_sum_user': 5,
            'new_cum_sum_bot': 3,
            'global_hits': ['hit1', 'hit2']
        })

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_result)
        mock_update_summary.assert_called_once_with('123', 5, 3, ['hit1', 'hit2'])

if __name__ == '__main__':
    unittest.main()
