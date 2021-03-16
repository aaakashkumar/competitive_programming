# Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/
# @author Akash Kumar

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode, lower_bound=-float('inf'), 
                   upper_bound=float('inf')) -> bool:
        
        if root is None:
            return True
        
        if root.val <= lower_bound or root.val >= upper_bound:
            return False
        
        else:
            return self.isValidBST(root.left, lower_bound, root.val) and \
                   self.isValidBST(root.right, root.val, upper_bound)
        