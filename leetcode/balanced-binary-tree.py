# Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/
# @author Akash Kumar

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def checkBalanced(node, is_balanced=True):
            # funny thing: using not node instead of node is None
            # makes the program wayyyy slower
            if node is None or not is_balanced:
                return (is_balanced, 0)
            
            is_balanced, left_height = checkBalanced(node.left, is_balanced)
            is_balanced, right_height = checkBalanced(node.right, is_balanced)
            
            if abs(left_height - right_height) > 1:
                is_balanced = False
                
            return (is_balanced, max(left_height, right_height) + 1)
                
                
        return bool(checkBalanced(root)[0])