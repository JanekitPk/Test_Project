from codes.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_2_3_5_is_prime(self):
        prime_list =[2, 3, 5]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_min_2_3_5_is_prime(self):
        prime_list = [-2, -3, -5]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_give_0_1_not_prime(self):
        prime_list = [0, 1]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_4_6_8_not_prime(self):
        prime_list = [4, 6, 8]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_give_min_4_6_8_not_prime(self):
        prime_list = [-4, -6, -8]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)        

