# Kth to Last Node in a Singly-Linked List
# https://www.interviewcake.com/question/python3/kth-to-last-node-in-singly-linked-list?course=fc1&section=linked-lists
# @author Akash Kumar


import unittest


def kth_to_last_node(k, head):
    
    if head == None:
        raise Exception("Linked List is empty")
    
    current_node = head  # the right node
    
    # set current_node to the kth node from the head
    while k > 1:
        current_node = current_node.next
        k -= 1
        
    if k != 1:
        # in case k nodes are not present
        raise Exception("There are less than k nodes in the Linked List")
        
    k_behind_current_node = head  # the left node
    
    # move both nodes to the next node, one step at a time
    while current_node.next != None:
        current_node = current_node.next
        k_behind_current_node = k_behind_current_node.next
    
    # Return the kth to last node in the linked list 
    return k_behind_current_node


















# Tests

class Test(unittest.TestCase):

    class LinkedListNode(object):

        def __init__(self, value, next=None):
            self.value = value
            self.next  = next

        def get_values(self):
            node = self
            values = []
            while node is not None:
                values.append(node.value)
                node = node.next
            return values

    def setUp(self):
        self.fourth = Test.LinkedListNode(4)
        self.third = Test.LinkedListNode(3, self.fourth)
        self.second = Test.LinkedListNode(2, self.third)
        self.first = Test.LinkedListNode(1, self.second)

    def test_first_to_last_node(self):
        actual = kth_to_last_node(1, self.first)
        expected = self.fourth
        self.assertEqual(actual, expected)

    def test_second_to_last_node(self):
        actual = kth_to_last_node(2, self.first)
        expected = self.third
        self.assertEqual(actual, expected)

    def test_first_node(self):
        actual = kth_to_last_node(4, self.first)
        expected = self.first
        self.assertEqual(actual, expected)

    def test_k_greater_than_linked_list_length(self):
        with self.assertRaises(Exception):
            kth_to_last_node(5, self.first)

    def test_k_is_zero(self):
        with self.assertRaises(Exception):
            kth_to_last_node(0, self.first)


unittest.main(verbosity=2)