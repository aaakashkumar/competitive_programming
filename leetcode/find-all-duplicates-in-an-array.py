# Find All Duplicates in an Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# @author Akash Kumar

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for index, value in enumerate(nums):
            if nums[abs(value)-1] < 0:
                duplicates.append(abs(value))
            else:
                nums[abs(value)-1] *= -1
        
        return duplicates