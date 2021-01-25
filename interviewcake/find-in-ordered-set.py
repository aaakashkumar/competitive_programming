# Find in Ordered Set
# https://www.interviewcake.com/question/python3/find-in-ordered-set?course=fc1&section=combinatorics-probability-math
# @author Akash Kumar


import unittest


def contains(ordered_list, number):

    # Check if an integer is present in the list
    left = 0
    right = len(ordered_list)-1
    
    # Binary Search
    while left <= right:
        mid = (left+right) // 2
        
        if ordered_list[right] < number or \
        ordered_list[left] > number:
            return False
        
        if ordered_list[mid] == number:
            return True
        
        else:
            if ordered_list[mid] > number:
                right = mid - 1
                    
            elif ordered_list[mid] < number:
                left = mid + 1
                

    return False


















# Tests

class Test(unittest.TestCase):

    def test_empty_list(self):
        result = contains([], 1)
        self.assertFalse(result)

    def test_one_item_list_number_present(self):
        result = contains([1], 1)
        self.assertTrue(result)

    def test_one_item_list_number_absent(self):
        result = contains([1], 2)
        self.assertFalse(result)

    def test_small_list_number_present(self):
        result = contains([2, 4, 6], 4)
        self.assertTrue(result)

    def test_small_list_number_absent(self):
        result = contains([2, 4, 6], 5)
        self.assertFalse(result)

    def test_large_list_number_present(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
        self.assertTrue(result)

    def test_large_list_number_absent(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
        self.assertFalse(result)

    def test_large_list_number_first(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertTrue(result)

    def test_large_list_number_last(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        self.assertTrue(result)


unittest.main(verbosity=2)