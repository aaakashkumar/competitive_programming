# The Stolen Breakfast Drone
# https://www.interviewcake.com/question/python3/find-unique-int-among-duplicates?course=fc1&section=bit-manipulation
# @author Akash Kumar


import unittest


def find_unique_delivery_id(delivery_ids):

    # Find the one unique ID in the list
    unique_delivery_id = 0
    
    # XOR through the list
    # duplicates will cancel out to 0
    # the unique number will be left
    for i in delivery_ids:
        unique_delivery_id ^= i

    return unique_delivery_id


















# Tests

class Test(unittest.TestCase):

    def test_one_drone(self):
        actual = find_unique_delivery_id([1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_first(self):
        actual = find_unique_delivery_id([1, 2, 2])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_comes_last(self):
        actual = find_unique_delivery_id([3, 3, 2, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_unique_id_in_middle(self):
        actual = find_unique_delivery_id([3, 2, 1, 2, 3])
        expected = 1
        self.assertEqual(actual, expected)

    def test_many_drones(self):
        actual = find_unique_delivery_id([2, 5, 4, 8, 6, 3, 1, 4, 2, 3, 6, 5, 1])
        expected = 8
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)