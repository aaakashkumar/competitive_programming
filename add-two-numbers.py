# https://leetcode.com/problems/add-two-numbers/
# @author Akash Kumar

from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Main method to solve the given problem
        :param l1: First Linked List's starting node
        :param l2: Second Linked List's starting node
        :return sum_list: The sum of l1 and l2
        """
        carry = 0
        sum_list = root = ListNode(0)

        while l1 is not None or l2 is not None:
            digit_sum = (0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + carry
            
            if digit_sum > 9:
                digit_sum = digit_sum % 10
                carry = 1
            else:
                carry = 0
            
            sum_list.next = ListNode(digit_sum)
            sum_list = sum_list.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        
        if carry != 0:
            sum_list.next = ListNode(carry)
            sum_list = sum_list.next
        
        return root.next

    def list_to_linked_list(self, list_):
        """
        Utility method to convert a python list to a Linked List
        :param list_: A list of numbers
        :return linked_list: A linked list made from the elements of list_
        """
        # https://stackoverflow.com/a/54880245/6722799

        current_node = root = ListNode(0)
        for item in list_:
            current_node.next = ListNode(item)
            current_node = current_node.next
        
        return root.next

    def linked_list_to_list(self, linked_list):
        """
        Utility method to convert a Linked List to a python list
        :param linked_list: A Linked List
        :return list_: A list made from the elements of linked_list
        """
        list_ = list()

        while linked_list is not None:
            list_.append(linked_list.val)
            linked_list = linked_list.next
        
        return list_

    def print_linked_list(self, linked_list):
        """
        Utility method to print a linked list
        :param linked_list: A Linked List
        """
        print('[', end=' ')
        while linked_list is not None:
            print(linked_list.val, end=' ')
            linked_list = linked_list.next
        print(']')
            
    def testAddTwoNumbers(self):
        """
        Method to test addTwoNumbers with a few sample test cases
        """
        # aliases to shorten the names
        list2ll = self.list_to_linked_list
        printll = self.print_linked_list
        ll2list = self.linked_list_to_list
        add2num = self.addTwoNumbers

        # sample test cases
        assert ll2list(add2num(list2ll([2,4,3]), list2ll([5,6,4]))) == [7,0,8]
        assert ll2list(add2num(list2ll([0]), list2ll([0]))) == [0]
        assert ll2list(add2num(list2ll([9,9,9,9,9,9,9]), list2ll([9,9,9,9]))) == [8,9,9,9,0,0,0,1]
        
        print("All test cases ran successfully")


Solution().testAddTwoNumbers()