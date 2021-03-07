# Path Sum
# https://leetcode.com/problems/path-sum/
# @author Akash Kumar

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root is None:
            return False
        
        def checkPathSum(node, current_sum):
            # use DFS to check if the path sum exists
            if node is None:
                return False
                
            if node.left is None and node.right is None:
                current_sum += node.val
                return current_sum == targetSum
            
            current_sum += node.val
            return checkPathSum(node.left, current_sum) or checkPathSum(node.right, current_sum)
            
        return checkPathSum(root, 0)