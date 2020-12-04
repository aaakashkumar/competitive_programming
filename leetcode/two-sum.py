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

        hash = {}
        for index, element in enumerate(nums):
            complement = target - element
            if complement in hash:
                return [index, hash[complement]]
            else:
                hash[element] = index
    
    def test_twoSum(self):
        """
        Method to test our twoSum solution
        """
        assert set(self.twoSum([2,7,11,15], 9)) == set([0, 1])
        assert set(self.twoSum([3,2,4], 6)) == set([1, 2])
        assert set(self.twoSum([3,3], 6)) == set([0, 1])
        print("All sample cases passed")

Solution().test_twoSum()