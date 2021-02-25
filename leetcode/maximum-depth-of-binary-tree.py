# Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# @author Akash Kumar


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0

        left_depth = self.maxDepth(root.left) if root.left else 0
        right_depth = self.maxDepth(root.right) if root.right else 0
        
        return max(left_depth, right_depth) + 1