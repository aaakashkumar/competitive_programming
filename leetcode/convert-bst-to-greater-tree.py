# Convert BST to Greater Tree
# https://leetcode.com/problems/convert-bst-to-greater-tree/
# @author Akash Kumar
# companies: MakeMyTrip

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0
        def greaterTree(node, greater_sum=None):
            nonlocal total
            
            if node is None:
                return
            
            greaterTree(node.right)
            total += node.val
            node.val = total
            greaterTree(node.left)
        
        greaterTree(root)
        return root