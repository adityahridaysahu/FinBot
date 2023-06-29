import unittest
from unittest.mock import MagicMock, patch
from flask import Flask, json
from bond_routes import app, bonds_api
from bond_service import BondService
from bond_dao import BondDAO

class TestBondRoutes(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.add_url_rule('/bonds-api', 'bonds_api', bonds_api, methods=['POST'])
        self.client = self.app.test_client()

    @patch.object(BondDAO, 'connect_to_database')  # Mock the database connection function
    @patch.object(BondDAO, 'execute_query')
    def test_bonds_api_endpoint(self, mock_execute_query, mock_connect_to_database):
        # Prepare test data
        mock_result = [
            {
                'isin': '1234567890',
                'category': 'Category 1',
                'currency_of_issue': 'USD',
                'coupon_rate': 4.5,
                'maturity': 10,
                'isOfferedByGS': 'Yes'
            },
            {
                'isin': '0987654321',
                'category': 'Category 2',
                'currency_of_issue': 'EUR',
                'coupon_rate': 3.2,
                'maturity': 5,
                'isOfferedByGS': 'No'
            }
        ]
        mock_execute_query.return_value = mock_result
        mock_connect_to_database.return_value = MagicMock()  # Mock the database connection

        # Send a POST request to the endpoint
        response = self.client.post('/bonds-api', json={'sql_query': 'SELECT * FROM bonds'})

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, mock_result)
        mock_execute_query.assert_called_once_with('SELECT * FROM bonds')
  
if __name__ == '__main__':
    unittest.main()
