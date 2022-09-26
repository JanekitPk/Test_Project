from codes.superfizzbuzz import *
import unittest

class SuperFizzBuzzTest(unittest.TestCase):
    def test_give_3_is_fizz(self):
        number = 3
        expected_result = 'Fizz'
        result = superfizzbuzz(number)
        self.assertEqual(result,expected_result)
        
    def test_give_5_is_buzz(self):
        number = 5
        expected_result = 'Buzz'
        result = superfizzbuzz(number)
        self.assertEqual(result,expected_result)

    def test_give_15_is_fizzbuzz(self):
        number = 15
        expected_result = 'FizzBuzz'
        result = superfizzbuzz(number)
        self.assertEqual(result,expected_result)

    def test_give_9_is_fizzfizz(self):
        number = 9
        expected_result = 'FizzFizz'
        result = superfizzbuzz(number)
        self.assertEqual(result,expected_result)

    def test_give_25_is_buzzbuzz(self):
        number = 25
        expected_result = 'BuzzBuzz'
        result = superfizzbuzz(number)
        self.assertEqual(result,expected_result)
    
    def test_give_225_is_fizzfizzbuzzbuzz(self):
        number = 225
        expected_result = 'FizzFizzBuzzBuzz'
        result = superfizzbuzz(number)
        self.assertEqual(result,expected_result)
