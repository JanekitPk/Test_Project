from codes.cipher import caesarCipher
import unittest

class AlternatingCharTest(unittest.TestCase):
    def test_middleOutz_5_give_okffngQwvb(self):
        string = 'middle-Outz'
        shift_num = 2
        expected_result = 'okffng-Qwvb'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)