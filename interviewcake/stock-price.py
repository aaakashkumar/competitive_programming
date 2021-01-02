# https://www.interviewcake.com/question/python3/stock-price?course=fc1&section=greedy
# @author Akash Kumar

def get_max_profit(stock_prices):

    if len(stock_prices) < 2:
        raise Exception

    # Calculate the max profit
    buy_price = stock_prices[0]
    sell_price = stock_prices[1]
    profit = sell_price - buy_price
    index = 1
    
    while index <= len(stock_prices)-1:
        if sell_price - buy_price > profit:
            profit = sell_price - buy_price

        if sell_price < buy_price:
            buy_price = sell_price

        index += 1
        try:
            sell_price = stock_prices[index]
        except:
            break

    return profit


















# Tests

import unittest

class Test(unittest.TestCase):

    def test_price_goes_up_then_down(self):
        actual = get_max_profit([1, 5, 3, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_price_goes_down_then_up(self):
        actual = get_max_profit([7, 2, 8, 9])
        expected = 7
        self.assertEqual(actual, expected)

    def test_price_goes_up_all_day(self):
        actual = get_max_profit([1, 6, 7, 9])
        expected = 8
        self.assertEqual(actual, expected)

    def test_price_goes_down_all_day(self):
        actual = get_max_profit([9, 7, 4, 1])
        expected = -2
        self.assertEqual(actual, expected)

    def test_price_stays_the_same_all_day(self):
        actual = get_max_profit([1, 1, 1, 1])
        expected = 0
        self.assertEqual(actual, expected)

    def test_error_with_empty_prices(self):
        with self.assertRaises(Exception):
            get_max_profit([])

    def test_error_with_one_price(self):
        with self.assertRaises(Exception):
            get_max_profit([1])


unittest.main(verbosity=2)