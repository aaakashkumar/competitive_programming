# Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# @author Akash Kumar

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

		def arrayToTree(lower_bound, upper_bound):
			"""
			Nested method to recursively find the left and right nodes and subnodes of a node.
			:param lower_bound: The lower bound within which the current node should exist
			:param upper_bound: The upper bound within which the current node should exist
			"""
			nonlocal node_index

			if lower_bound > upper_bound:
				return None
			
			current_node_value = preorder[node_index]
			node = TreeNode(current_node_value)
			node_index += 1

			node.left = arrayToTree(lower_bound, inorder_index_map[current_node_value]-1)
			node.right = arrayToTree(inorder_index_map[current_node_value]+1, upper_bound)

			return node

		# initial settings
		node_index = 0  # to be used as a global variable by the arrayToTree method
		inorder_index_map = dict()
		for index, value in enumerate(inorder):
			inorder_index_map[value] = index

		return arrayToTree(0, len(preorder)-1)


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