# Permutations
# https://leetcode.com/problems/permutations/
# @author Akash Kumar

from typing import List


class Solution:
	def permute(self, nums: List[int]) -> List[List[int]]:

		def directed_permutations(nums, current_swap_index=0):
			"""
			Takes the first element of the array or sub-array, and generates a 
			permutation with the rest of the elements. Saves the result to `result` list
			"""

			if current_swap_index == len(nums) - 1:
				result.append(nums.copy())
				return

			for next_swap_index in range(current_swap_index, len(nums)):
				nums[current_swap_index], nums[next_swap_index] = \
				nums[next_swap_index], nums[current_swap_index]

				directed_permutations(nums, current_swap_index+1)

				nums[current_swap_index], nums[next_swap_index] = \
				nums[next_swap_index], nums[current_swap_index]

		result = []
		directed_permutations(nums)
		return result

	def testPermute(self):
		"""
		A method to test permute()
		"""
		# print(self.permute([1,2,3]))
		assert sorted(self.permute([1,2,3])) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
		assert sorted(self.permute([0,1])) == sorted([[0,1],[1,0]])
		assert sorted(self.permute([1])) == sorted([[1]])

		print("All sample test cases ran successfully")


Solution().testPermute()