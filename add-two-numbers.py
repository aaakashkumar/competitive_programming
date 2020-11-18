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
        addend = 0
        sum_list = root = ListNode(0)

        while l1 is not None and l2 is not None:
            digit_sum = l1.val + l2.val + addend
            
            if digit_sum > 9:
                digit_sum = digit_sum % 10
                addend = 1
            else:
                addend = 0
            
            sum_list.next = ListNode(digit_sum)
            sum_list = sum_list.next

            l1 = l1.next
            l2 = l2.next

            if l1 is None and l2 is not None:
                while l2 is not None:
                    sum_list.next = ListNode(l2.val + addend)
                    sum_list = sum_list.next
                    if sum_list.val > 9:
                        sum_list.val = sum_list.val % 10
                        addend = 1
                    else:
                        addend = 0
                    l2 = l2.next
                break

            if l2 is None and l1 is not None:
                while l1 is not None:
                    sum_list.next = ListNode(l1.val + addend)
                    sum_list = sum_list.next
                    if sum_list.val > 9:
                        sum_list.val = sum_list.val % 10
                        addend = 1
                    else:
                        addend = 0
                    l1 = l1.next
                break
        
        return root.next

    def list_to_linked_list(self, list_):
        # https://stackoverflow.com/a/54880245/6722799

        current_node = root = ListNode(0)
        for item in list_:
            current_node.next = ListNode(item)
            current_node = current_node.next
        
        return root.next

    def linked_list_to_list(self, linked_list):
        list_ = list()
        while linked_list is not None:
            list_.append(linked_list.val)
            linked_list = linked_list.next
        
        return list_

    def print_linked_list(self, linked_list):
        print('[', end=' ')
        while linked_list is not None:
            print(linked_list.val, end=' ')
            linked_list = linked_list.next
        print(']')
            
    def testAddTwoNumbers(self):
        list2ll = self.list_to_linked_list
        printll = self.print_linked_list
        ll2list = self.linked_list_to_list
        add2num = self.addTwoNumbers

        assert ll2list(add2num(list2ll([2,4,3]), list2ll([5,6,4]))) == [7,0,8]
        assert ll2list(add2num(list2ll([0]), list2ll([0]))) == [0]
        printll(add2num(list2ll([9,9,9,9,9,9,9]), list2ll([9,9,9,9])))
        assert ll2list(add2num(list2ll([9,9,9,9,9,9,9]), list2ll([9,9,9,9]))) == [8,9,9,9,0,0,0,1]
        
        print("All test cases ran successfully")

Solution().testAddTwoNumbers()