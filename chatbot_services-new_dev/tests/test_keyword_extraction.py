import unittest
from tools.keyword_extractor import keyword_extractor

class TestExtractKeywords(unittest.TestCase):

   def test_keyword_extractor(self):
       sentence = "What are the types of bonds in the financial market?"
       expected_keywords = ['types', 'bonds', 'financial', 'market']

       keywords = keyword_extractor(sentence)

       self.assertEqual(keywords, expected_keywords)

   def test_keyword_extractor_empty_sentence(self):
       sentence = ""
       expected_keywords = []

       keywords = keyword_extractor(sentence)

       self.assertEqual(keywords, expected_keywords)

   def test_keyword_extractor_special_characters(self):
       sentence = "I love @python and #programming!"
       expected_keywords = ['love', '@', 'python', 'programming']
       keywords = keyword_extractor(sentence)

       self.assertEqual(keywords, expected_keywords)

if __name__ == '__main__':
   unittest.main()