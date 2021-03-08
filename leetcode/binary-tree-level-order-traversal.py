# Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/
# @author Akash Kumar

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        nodes = [[root]]
        node_values = [[root.val]]
        
        while True:
            parent_level_nodes = nodes[-1]
            
            current_nodes = list()
            current_node_values = list()
            
            for node in parent_level_nodes:
                if node.left:
                    current_nodes.append(node.left)
                    current_node_values.append(node.left.val)
                if node.right:
                    current_nodes.append(node.right)
                    current_node_values.append(node.right.val)
            
            if len(current_node_values) == 0:
                break
                
            nodes.append(current_nodes)
            node_values.append(current_node_values)
            
        return node_values
            
            