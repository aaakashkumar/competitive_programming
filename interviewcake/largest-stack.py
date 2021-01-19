# Largest Stack
# https://www.interviewcake.com/question/python3/largest-stack?course=fc1&section=queues-stacks
# @author Akash Kumar

import unittest


class Stack(object):

    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)

    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()

    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


class MaxStack(object):

    # Implement the push, pop, and get_max methods


    def __init__(self):
        self.stack = Stack()
        self.max_stack = Stack()

    def push(self, item):
        try:
            if self.stack.peek() is None:
                self.max_stack.push(item)
                
            elif item >= self.max_stack.peek():
                self.max_stack.push(item)
                
            self.stack.push(item)
                
        
        except Exception as e:
            print("An error occurred while trying to push to the Stack:\n", e)

    def pop(self):
        if self.stack.peek():
            popped_item = self.stack.pop()
            if popped_item == self.max_stack.peek():
                self.max_stack.pop()
            
            return popped_item
        
        else:
            raise Exception("No items are present in the Stack")
            

    def get_max(self):
        return self.max_stack.peek()


class MaxStackBonus(object):
    """
    This class implements solution to the bonus problem, i.e., to 
    implement the MaxStack in O(1) time and O(1) additional space

    Logic:
    The logic is similar to what's given here: 
    https://www.geeksforgeeks.org/find-maximum-in-a-stack-in-o1-time-and-o1-extra-space/

    However, no need to do a complicated (2*x – maxEle) as described
    
    The following simple equations are way easier to understand:
    1. top = previous max + current max
        when pushing into the stack, update top as the above in case a new max is found

    2. previous max = top - current max
        while popping, just do the above to get the previous maximum value
    """


    def __init__(self):
        self.stack = Stack()
        self.maxItem = None

    def push(self, item):
        if self.stack.peek() is None:
            self.stack.push(item)
            self.maxItem = item
            
        else:
            if item > self.maxItem:
                # top = previous max + current max
                self.stack.push(item + self.maxItem)
                self.maxItem = item
                
            else:
                self.stack.push(item)

    def pop(self):
        if self.stack.peek() is None:
            return None
            
        if self.stack.peek() > self.maxItem:
            temp = self.maxItem  # the value to be returned

            # previous max = top - current max
            self.maxItem = self.stack.peek() - self.maxItem

            self.stack.pop()
            return temp
            
        else:
            return self.stack.pop()

    def get_max(self):
        return self.maxItem

















# Tests

class Test(unittest.TestCase):

    def test_stack_usage(self):
        max_stack = MaxStack()

        max_stack.push(5)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        max_stack.push(4)
        max_stack.push(7)
        max_stack.push(7)
        max_stack.push(8)

        actual = max_stack.get_max()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 4
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

    def test_bonus_stack_usage(self):
        max_stack = MaxStackBonus()

        max_stack.push(5)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        max_stack.push(4)
        max_stack.push(7)
        max_stack.push(7)
        max_stack.push(8)

        actual = max_stack.get_max()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 8
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 7
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)

        actual = max_stack.pop()
        expected = 4
        self.assertEqual(actual, expected)

        actual = max_stack.get_max()
        expected = 5
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)