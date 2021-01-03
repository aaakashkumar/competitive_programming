# https://www.interviewcake.com/question/python3/product-of-other-numbers?course=fc1&section=greedy
# @author Akash Kumar

import unittest


def get_products_of_all_ints_except_at_index(int_list):

    # Make a list with the products
    left_elements_product = [1]*len(int_list)
    right_elements_product = [1]*len(int_list)

    left_pointer = 1
    right_pointer = len(int_list)-2

    left_elements_product[0] = int_list[0]
    right_elements_product[len(int_list)-1] = int_list[len(int_list)-1]

    while left_pointer < len(int_list)-1:
        left_elements_product[left_pointer] = int_list[left_pointer] * \
                                                left_elements_product[left_pointer-1]
        right_elements_product[right_pointer] = int_list[right_pointer] * \
                                                right_elements_product[right_pointer+1]

        left_pointer += 1
        right_pointer -= 1

    result_list = []
    result_list.append(right_elements_product[1])

    for index in range(1, len(int_list)-1):
        result_list.append(left_elements_product[index-1] * right_elements_product[index+1])

    result_list.append(left_elements_product[len(int_list)-1-1])


    return result_list


















# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)