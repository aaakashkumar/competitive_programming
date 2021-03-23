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
        """
        Method to convert a BST to a Greater Sum BST using 
        recursive reverse inorder traversal.
        """
        total = 0  # global total

        def greaterTree(node, greater_sum=None):
            nonlocal total
            
            if node is None:
                return
            
            # go Right -> Root -> Left
            greaterTree(node.right)
            total += node.val
            node.val = total
            greaterTree(node.left)
        
        greaterTree(root)
        return root

    def convertBSTAlternate(self, root: TreeNode) -> TreeNode:
        """
        Method to convert a BST to a Greater Sum BST using 
        Reverse Morris inorder traversal.

        Good resources for Morris Traversal:
        - CppCon 2017 https://www.youtube.com/watch?v=YA-nB2wjVcI&t=702s
        - Educative.io https://www.educative.io/edpresso/what-is-morris-traversal
        """

        total = 0  # global total
        node = root
        
        while node is not None:
            # traverse left if there is no right child
            if node.right is None:
                total += node.val
                node.val = total
                node = node.left
            
            # if there is a right child
            else:
                # find the leftmost node of the right node of the current node
                leftmost_node_of_right = node.right
                while leftmost_node_of_right.left is not None and \
                      leftmost_node_of_right.left is not node:
                    leftmost_node_of_right = leftmost_node_of_right.left
                
                # if there is no left child of the leftmost node, set the 
                # current node as the leftmost node's child. This will help
                # in coming back to the current node without the need of 
                # additional space
                if leftmost_node_of_right.left is None:
                    leftmost_node_of_right.left = node
                    node = node.right
                
                # if there is a left child of the leftmost node, which is 
                # equal to the current node, it means we've already visited
                # this node, and the left child is the backline that we
                # created before
                else:
                    total += node.val
                    node.val = total
                    node = node.left
                    leftmost_node_of_right.left = None
                    
        return root