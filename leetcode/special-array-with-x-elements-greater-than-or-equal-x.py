# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
# @author Akash Kumar

from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        """
        param nums: Array of integers
        """
        nums = sorted(nums)
        nums_len = len(nums)
            
        gt_eq_current_value = 0  # number of elements greater or equal to the current value

        for index, value in enumerate(nums):
            if index>0 and nums[index-1] == nums[index]: continue

            while gt_eq_current_value <= value:
                if gt_eq_current_value == nums_len-index:
                    return gt_eq_current_value
                gt_eq_current_value += 1
        
        return -1

    def testSpecialArray(self):
        assert self.specialArray([3,5]) == 2
        assert self.specialArray([0,0]) == -1
        assert self.specialArray([0,4,3,0,4]) == 3
        assert self.specialArray([3,6,7,7,0]) == -1
        print("All test cases ran successfully")

Solution().testSpecialArray()