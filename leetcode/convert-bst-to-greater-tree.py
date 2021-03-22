# Convert BST to Greater Tree
# https://leetcode.com/problems/convert-bst-to-greater-tree/
# @author Akash Kumar

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        def greaterTree(node, greater_sum=None):
            """
            The basic idea here is described in points below
            - basically you have to go in a reverse inorder style to add up all
              the greater values of a node
            - the values in the right subtree of a node are greater than the node
            - sum up all the values in the right subtree, which is the sum to be added to 
              the current node
            - the current node, inclusive of its children, may be a right subtree of a parent
            - so return the sum of the current node, its right subtree, and its left subtree, 
              to its parent node
            - when calling the left subtree, note that the current node, as well as the values
              in the right subtree are all greater than the left subtree
            - so, the sum of the current node value and the right subtree sum is then passed 
              down to the left subtree too
            - nodes in the left subtree add this value to itself, however, do not return this value;
              they return the original value instead
            - also, even if a node is in the right subtree of a parent node, the parent node may
              be a left subtree to a node x, so all the values of node x will be greater than the
              current node
            - overall, the greater sum is passed down the tree, and the original sum is passed
              up in the tree
            """
            if node is None:
                return 0
            
            right_original_sum = greaterTree(node.right, greater_sum=greater_sum)
            current_original_sum = right_original_sum + node.val
            node.val = current_original_sum + (greater_sum or 0)
            left_original_sum = greaterTree(node.left, greater_sum=node.val)

            return (left_original_sum+current_original_sum)
        
        greaterTree(root)
        return root