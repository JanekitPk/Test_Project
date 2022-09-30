from codes.alternatingchar import alternatingCharacters
import unittest

class AlternatingCharTest(unittest.TestCase):
    def test_AAAA_give_3(self):
        string = 'AAAA'
        expected_result = 3
        result = alternatingCharacters(string)
        self.assertEqual(result,expected_result)

    def test_BBBBB_give_4(self):
        string = 'BBBBB'
        expected_result = 4
        result = alternatingCharacters(string)
        self.assertEqual(result,expected_result)

    def test_ABABABAB_give_0(self):
        string = 'ABABABAB'
        expected_result = 0
        result = alternatingCharacters(string)
        self.assertEqual(result,expected_result)

    def test_BABABA_give_0(self):
        string = 'BABABA'
        expected_result = 0
        result = alternatingCharacters(string)
        self.assertEqual(result,expected_result)

    def test_AAABBB_give_4(self):
        string = 'AAABBB'
        expected_result = 4
        result = alternatingCharacters(string)
        self.assertEqual(result,expected_result)