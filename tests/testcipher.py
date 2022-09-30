from codes.cipher import caesarCipher
import unittest

class AlternatingCharTest(unittest.TestCase):
    def test_middleOutz_give_okffngQwvb(self):
        string = 'middle-Outz'
        expected_result = 'okffng-Qwvb'
        result = caesarCipher(string)
        self.assertEqual(result,expected_result)