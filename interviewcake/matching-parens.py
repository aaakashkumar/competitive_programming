# Parenthesis Matching
# https://www.interviewcake.com/question/c/matching-parens?course=fc1&section=queues-stacks
# @author Akash Kumar


import unittest


def get_closing_paren(sentence, opening_paren_index):
    """
    Find the position of the matching closing parenthesis
    
    :param sentence: The sentence in which the closing parenthesis is
    to be searched
    :param opening_paren_index: the position of an opening parenthesis
    in the string
    """
    
    parenthesis_stack_count = 1
    
    while parenthesis_stack_count != 0 and opening_paren_index < len(sentence)-1:
        opening_paren_index += 1
        
        if sentence[opening_paren_index] == '(':
            # this is equivalent to pushing into a Stack
            parenthesis_stack_count += 1
        
        elif sentence[opening_paren_index] == ')':
            # this is equivalent to popping from the Stack
            # in case a closing parenthesis is found
            parenthesis_stack_count -= 1
        
        
    if parenthesis_stack_count == 0:
        # if parenthesis_stack_count is 0, the closing parenthesis WAS found
        return opening_paren_index
    else:
        raise Exception("Closing parenthesis not found in the string")


















# Tests

class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)