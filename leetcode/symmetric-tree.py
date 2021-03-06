# Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
# @author Akash Kumar

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def checkSymmetric(leftnode, rightnode):
            if leftnode is None and rightnode is None:
                return True

            if leftnode and rightnode:
                return (leftnode.val == rightnode.val 
                        and checkSymmetric(leftnode.left, rightnode.right)
                        and checkSymmetric(leftnode.right, rightnode.left))
            
            # in case one of the left or right nodes is None
            return False
        
        return root and checkSymmetric(root.left, root.right)
            
                
                