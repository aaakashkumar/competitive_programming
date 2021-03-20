from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Method to construct and return the binary tree from its preorder and 
        inorder traversal.
        :param preorder: preorder traversal of a binary tree
        :param inorder: inorder traversal of the same tree
        """
        if len(preorder) == 0: return None
        if len(preorder) == 1: return TreeNode(preorder[0])

        def findChildren(lower_bound, upper_bound):
            """
            Nested method to recursively find the left and right nodes and subnodes of a node using the 
            inorder traversal of a tree. Given a node (defined by its index in the preorder traversal), the
            idea is to check whether the next node in the preorder traversal, is a root in the left subtree 
            of the current node or a root in the right subtree of the current node. This can be checked by 
            seeing whether the next node occurs to the left or right of the current node in the inorder traversal
            of the tree.
            :param lower_bound: The lower bound within which the current node should exist
            :param upper_bound: The upper bound within which the current node should exist
            """
            nonlocal node_index
            
            node = TreeNode(preorder[node_index])

            # base condition: leaf node is found
            if lower_bound == upper_bound or node_index >= len(preorder) or node_index < 0:
                return node

            # find the current node's position (index) in the inorder traversal of the tree
            node_position_in_inorder = inorder.index(preorder[node_index], lower_bound,
                                                     upper_bound+1)

            # find left node
            node_index += 1	
            if node_index < len(preorder) and \
            preorder[node_index] in inorder[lower_bound:node_position_in_inorder-1+1]:
                # if the next node exists in the left of the current node's inorder traversal index, 
                # continue finding it's further nodes
                node.left = findChildren(lower_bound, node_position_in_inorder-1)
            else:
                # in case the next element is not present on the left of the node in the inorder traversal
                node_index -= 1
                node.left = None

            # find right node
            node_index += 1	
            if node_index < len(preorder) and \
            preorder[node_index] in inorder[node_position_in_inorder+1:upper_bound+1]:
                # if the next node exists in the right of the current node's inorder traversal index, 
                # continue finding it's further nodes
                node.right = findChildren(node_position_in_inorder+1, upper_bound)
            else:
                # in case the next element is not present on the right of the node in the inorder traversal
                node_index -= 1
                node.right = None

            return node

        # initial settings
        node_index = 0  # to be used as a global variable by the findChildren function
        lower_bound = 0 # the lower limit of the bound between which the next node is to be searched
        upper_bound = len(preorder)-1  # the lower limit of the bound between which the next node is to be searched

        root = TreeNode(preorder[0])
        root_position_in_inorder = inorder.index(preorder[0])

        node_index += 1
        if root_position_in_inorder > 0 and \
        preorder[node_index] in inorder[lower_bound:root_position_in_inorder-1+1]:
            root.left = findChildren(lower_bound, root_position_in_inorder-1)
        else:
            node_index -= 1
            root.left = None
        
        node_index += 1
        if node_index < len(preorder) and \
        preorder[node_index] in inorder[root_position_in_inorder+1:upper_bound+1]:
            root.right = findChildren(root_position_in_inorder+1, upper_bound)
        else:
            node_index -= 1
            root.right = None

        return root

"""
Sample test cases:

[3,9,20,15,7]
[9,3,15,20,7]
[1,2]
[1,2]
[1,2]
[2,1]
[3,2,1,4]
[1,2,3,4]
"""