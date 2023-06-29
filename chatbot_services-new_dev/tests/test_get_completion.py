import unittest
from tools.get_completion import get_completion

class TestGetCompletion(unittest.TestCase):

   def test_get_completion_working(self):
       prompt = "What is the capital of France?"

       completion = get_completion(prompt)

       self.assertEqual(completion["status"], "working")
       self.assertNotEqual(completion["content"], "")

if __name__ == '__main__':
   unittest.main()