# Computer the nth Fibonacci number
# https://www.interviewcake.com/question/python3/nth-fibonacci?course=fc1&section=dynamic-programming-recursion
# @author Akash Kumar

import unittest


def fib(n):
    
    if n < 0:
        raise Exception("Can't find the " + str(n) + "th fibonacci number")

    if n == 0: return 0
    if n == 1: return 1

    x = 0
    y = 1
    nth = None

    # Compute the nth Fibonacci number
    for i in range(2, n+1):
        nth = x+y
        x, y = y, nth

    return nth


















# Tests

class Test(unittest.TestCase):

    def test_zeroth_fibonacci(self):
        actual = fib(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_first_fibonacci(self):
        actual = fib(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_second_fibonacci(self):
        actual = fib(2)
        expected = 1
        self.assertEqual(actual, expected)

    def test_third_fibonacci(self):
        actual = fib(3)
        expected = 2
        self.assertEqual(actual, expected)

    def test_fifth_fibonacci(self):
        actual = fib(5)
        expected = 5
        self.assertEqual(actual, expected)

    def test_tenth_fibonacci(self):
        actual = fib(10)
        expected = 55
        self.assertEqual(actual, expected)

    def test_negative_fibonacci(self):
        with self.assertRaises(Exception):
            fib(-1)


unittest.main(verbosity=2)