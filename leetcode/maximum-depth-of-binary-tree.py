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
    def __init__(self):
        # stores the maximum depth found
        self.max_depth = 0
        
    def maxDepth(self, root: TreeNode) -> int:
        def findMaxDepth(node, current_depth):
            if not node:
                return
                
            if not node.left and not node.right:
                self.max_depth = max(self.max_depth, current_depth)
                
            findMaxDepth(node.left, current_depth+1)
            findMaxDepth(node.right, current_depth+1)
        
        findMaxDepth(root, 1)
        return self.max_depth