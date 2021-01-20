# Implement A Queue with Two Stacks
# https://www.interviewcake.com/question/python3/queue-two-stacks?course=fc1&section=queues-stacks
# @author Akash Kumar


import unittest


class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        """
        Let's call our stacks in_stack and out_stack.

        """
        self.in_stack = []
        self.out_stack = []


    def enqueue(self, item):
        """
        For enqueue, we simply push the enqueued item onto in_stack.
        
        :param item: the item to be enqueued in the Queue
        """
        try:
            self.in_stack.append(item)
        except Exception as e:
            print("An error occurred while trying to enqueue.\n", e)
            

    def dequeue(self):
        """
        For dequeue on an empty out_stack, the oldest item is 
        at the bottom of in_stack. So we dig to the bottom of 
        in_stack by pushing each item one-by-one onto out_stack 
        until we reach the bottom item, which we return.
        
        :return: The frontmost value in the Queue 
        """
        if len(self.out_stack) == 0:
            if len(self.in_stack) == 0:
                raise Exception("No elements present in the Queue")
                
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())
                
        return self.out_stack.pop()


















# Tests

class Test(unittest.TestCase):

    def test_basic_queue_operations(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        queue.enqueue(4)

        actual = queue.dequeue()
        expected = 3
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 4
        self.assertEqual(actual, expected)

    def test_error_when_dequeue_from_new_queue(self):
        queue = QueueTwoStacks()

        with self.assertRaises(Exception):
            queue.dequeue()

    def test_error_when_dequeue_from_empty_queue(self):
        queue = QueueTwoStacks()

        queue.enqueue(1)
        queue.enqueue(2)

        actual = queue.dequeue()
        expected = 1
        self.assertEqual(actual, expected)

        actual = queue.dequeue()
        expected = 2
        self.assertEqual(actual, expected)

        with self.assertRaises(Exception):
            queue.dequeue()


unittest.main(verbosity=2)