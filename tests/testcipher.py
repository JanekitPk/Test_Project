from codes.cipher import caesarCipher
import unittest

class AlternatingCharTest(unittest.TestCase):
    def test_middleOutz_5_give_okffngQwvb(self):
        string = 'middle-Outz'
        shift_num = 2
        expected_result = 'okffng-Qwvb'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)

    def test_AxcZ_3_give_DafC(self):
        string = 'AxcZ+'
        shift_num = 3
        expected_result = 'DafC+'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)

    def test_asfsgrja_7_give_hzmznyqh(self):
        string = 'asfsgrja'
        shift_num = 7
        expected_result = 'hzmznyqh'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)

    def test_ndSENGSNnedl657_5_give_siXJSLXSsjiq657(self):
        string = 'ndSENGSNnedl657'
        shift_num = 5
        expected_result = 'siXJSLXSsjiq657'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)

    def test_fdjns14_6_give_ljpty14(self):
        string = 'fdjns14@'
        shift_num = 6
        expected_result = 'ljpty14@'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)

    def test_aZx_min1_give_zYw(self):
        string = 'aZx'
        shift_num = -1
        expected_result = 'zYw'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)

    def test_b_3_give_e(self):
        string = 'b'
        shift_num = 3
        expected_result = 'e'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)

    def test_C_4_give_G(self):
        string = 'C'
        shift_num = 4
        expected_result = 'G'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)

    def test_O_5_give_T(self):
        string = 'O'
        shift_num = 5
        expected_result = 'T'
        result = caesarCipher(string,shift_num)
        self.assertEqual(result,expected_result)