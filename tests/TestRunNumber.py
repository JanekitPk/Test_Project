from codes.Runnumber_util import FizzBuzz
import unittest

class FizzBuzzTest(unittest.TestCase):
    def test_give_3_is_fizz(self):
        number = 3
        expected_result = 'Fizz'
        result = FizzBuzz(number)
        self.assertEqual(result,expected_result)
        self.assertNotEqual(result,'Buzz')
        self.assertNotEqual(result,'FizzBuzz')

    def test_give_5_is_buzz(self):
        number = 5
        expected_result = 'Buzz'
        result = FizzBuzz(number)
        self.assertEqual(result,expected_result)
        self.assertNotEqual(result,'Fizz')
        self.assertNotEqual(result,'FizzBuzz')

    def test_give_15_is_fizzbuzz(self):
        number = 15
        expected_result = 'FizzBuzz'
        result = FizzBuzz(number)
        self.assertEqual(result,expected_result)
        self.assertNotEqual(result,'Fizz')
        self.assertNotEqual(result,'Buzz')
   
