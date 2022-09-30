from codes.twochar import alternate
import unittest

class AlternatingCharTest(unittest.TestCase):
    def test_give_beabeefeab_return_5(self):
        text = 'beabeefeab'
        expect_result = 5
        result = alternate(text)
        self.assertEqual(result, expect_result)
    
    def test_give_abaacdabd_return_4(self):
        text = 'abaacdabd'
        expect_result = 4
        result = alternate(text)
        self.assertEqual(result, expect_result)
    
    def test_give_aaabaa_return_0(self):
        text = 'aaabaa'
        expect_result = 0
        result = alternate(text)
        self.assertEqual(result, expect_result)
    
    def test_give_a_return_0(self):
        text = 'a'
        expect_result = 0
        result = alternate(text)
        self.assertEqual(result, expect_result)
    
    def test_give_aa_return_0(self):
        text = 'aa'
        expect_result = 0
        result = alternate(text)
        self.assertEqual(result, expect_result)
    
    def test_give_nonestr_return_0(self):
        text = ''
        expect = 0
        result = alternate(text)
        self.assertEqual(result, expect)
    
    