import unittest
from sympy import isprime
from is_prime_number import is_prime
from quadratic_sorting import *
from binary_search import binary_search


class TestCase(unittest.TestCase):
    """Tests for my algorithms."""

    def setUp(self):
        """Data for all test methods."""
        self.prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
        self.non_prime_list = [-1000, -22, 0, 1, 4, 100, 10000]
        self.some_numbers = [12, 83, -55, 100, 23, -102548]

    def test_is_true_prime_number(self):
        """Check primes"""
        for val in self.prime_list:
            self.assertTrue(is_prime(val))

    def test_is_false_prime_number(self):
        """Check non primes"""
        for val in self.non_prime_list:
            self.assertFalse(is_prime(val))

    def test_some_numbers_is_prime(self):
        for val in self.some_numbers:
            self.assertEqual(isprime(val), is_prime(val))

    def test_quadratic_sorting_insertion_sort(self):
        self.assertEqual(sorted(self.some_numbers),
                         insertion_sort(self.some_numbers))

    def test_quadratic_sorting_selection_sort(self):
        self.assertEqual(sorted(self.some_numbers),
                         selection_sort(self.some_numbers))

    def test_quadratic_sorting_bubble_sort(self):
        self.assertEqual(sorted(self.some_numbers),
                         bubble_sort(self.some_numbers))


class TestBinarySearch(unittest.TestCase):

    def testDuplicateElements(self):
        """
        Точно не знаю, должна ли функция возвращать результат 0 или 1.
        В данный ситуации вернет 1, но можно дописать в коде условие,
        чтобы проверяло, не является ли элемент слева таким же и тд.
        И тогда вернуть крайний левый похожий элемент.
        """
        self.assertEqual(binary_search([1, 1, 2, 2, 3, 3, 4], 1), 1,
                         'Problem with duplicate elements')

    def testListLen(self):
        self.assertEqual(binary_search([], 1), None, 'Problem with empty list')
        self.assertEqual(binary_search([5], 5), 0,
                         'Problem with one element in list')
        self.assertEqual(binary_search([5, 6], 6), 1,
                         'Problem with 2 elements in list')

    def testFirstLastElements(self):
        self.assertEqual(binary_search([0, 1, 2, 3, 4, 5], 0), 0,
                         'Problem with first element in the list')
        self.assertEqual(binary_search([0, 1, 2, 3, 4, 5], 5), 5,
                         'Problem with last element in the list')

    def testNotIn(self):
        self.assertEqual(binary_search([1, 2], 3), None, 'Element not in list')


if __name__ == '__main__':
    unittest.main()
