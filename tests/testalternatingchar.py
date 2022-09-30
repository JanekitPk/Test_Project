from codes.alternatingchar import alternatingCharacters
import unittest

class AlternatingCharTest(unittest.TestCase):
    def test_AAAA_give_3(self):
        string = 'AAAA'
        expected_result = 3
        result = alternatingCharacters(string)
        self.assertEqual(result,expected_result)