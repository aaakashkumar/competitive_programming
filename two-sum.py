# https://leetcode.com/problems/two-sum/
# @author Akash Kumar

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :param nums: A list of integers
        :param target: The target to sum up to
        :return: A list of integers, representing the minimum number of elements from the 
        list that can be summed to obtain target
        """

        nums = sorted(enumerate(nums), key=lambda x: x[1])

        left = 0
        right = len(nums) - 1

        while left < right:
            two_sum = nums[left][1] + nums[right][1]
            if two_sum == target:
                return [nums[left][0], nums[right][0]]

            elif two_sum > target:
                right -= 1

            elif two_sum < target:
                left += 1
    
    def test_twoSum(self):
        """
        Method to test our twoSum solution
        """
        assert self.twoSum([2,7,11,15], 9) == [0, 1]
        assert self.twoSum([3,2,4], 6) == [1, 2]
        assert self.twoSum([3,3], 6) == [0, 1]
        print("All sample cases passed")

Solution().test_twoSum()