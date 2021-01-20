# Bracket Validator
# https://www.interviewcake.com/question/python3/bracket-validator?course=fc1&section=queues-stacks
# @author Akash Kumar

import unittest


def is_valid(code):
    """
    Determine if the input code is valid
    """
    
    parenthesis_stack = []
    
    if code == "":
        return True
    
    closing_to_opening_bracket_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    opening_to_closing_bracket_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    
    for character in code:
        
        if character in closing_to_opening_bracket_map:
            if len(parenthesis_stack) == 0:
                return False
            if closing_to_opening_bracket_map[character] == parenthesis_stack[-1]:
                parenthesis_stack.pop()
            else:
                return False
            
        elif character in opening_to_closing_bracket_map:
            parenthesis_stack.append(character)
    
    if len(parenthesis_stack) > 0:
        return False
    else:
        return True


















# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)

    def test_actual_program(self):
        result = is_valid('#include <iostream>\nusing namespace std;\n\nint main() {\n  printf("Hello World");\n  return 0;\n}')
        self.assertTrue(result)


unittest.main(verbosity=2)