# Recursive String Permutations
# https://www.interviewcake.com/question/python3/recursive-string-permutations?course=fc1&section=dynamic-programming-recursion
# @author Akash Kumar


import unittest


def get_permutations(string):
    
    # base condition
    if len(string) <= 1:
        return set([string])
        
    first_char = string[0]
    rest_of_the_string = string[1:]
    
    permutations = set()
    
    # get all the permutations of the string without the first character
    permutations_of_rest = get_permutations(rest_of_the_string)
    
    # Generate all permutations of the input string
    for permutation in permutations_of_rest:
        
        # there will be len(permutation) + 1 places for the 
        # first character
        for i in range(len(permutation)+1+1):
            permutations.add(
                    permutation[:i] + first_char + permutation[i:]
                )

    return permutations


    return set()


















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)
    
    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)
    
    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)
    
    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)