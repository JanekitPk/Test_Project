from codes.cipher import caesarCipher
import unittest

class AlternatingCharTest(unittest.TestCase):
    def test_b_3_give_e(self):
        string = 'b'
        shift_num = 3
        expected_result = 'e'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)

class AlternatingCharTest(unittest.TestCase):
    def test_C_4_give_G(self):
        string = 'C'
        shift_num = 4
        expected_result = 'G'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)

class AlternatingCharTest(unittest.TestCase):
    def test_O_5_give_T(self):
        string = 'O'
        shift_num = 5
        expected_result = 'T'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)