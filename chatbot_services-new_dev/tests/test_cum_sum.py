import unittest
from unittest.mock import patch
import json
from tools.get_completion import get_completion
from tools.cumulative_summary import cumulative_summary

class TestCumulativeSummary(unittest.TestCase):
    @patch('tools.get_completion')
    def test_cumulative_summary_working_status(self, mock_get_completion):
        # Prepare test data
        unique_id = "1103ba0a-42"
        user_query = "What are the types of bonds in the financial market?"
        response = "Bot response"
        csum_bot = "Bot cumulative summary"
        csum_user = "User cumulative summary"

        mock_result = {
            "status": "working",
            "unique_ID": unique_id,
            "new_cum_sum_user" : "",
            "new_cum_sum_bot" : ""
        }
        mock_get_completion.return_value = mock_result

        # Call the function under test
        result = cumulative_summary(unique_id, user_query, response, csum_bot, csum_user)

        # Assertions
        self.assertEqual(result["status"], "working")
        self.assertEqual(result["unique_ID"], unique_id)

if __name__ == '__main__':
    unittest.main()
