# Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence
# @author Akash Kumar


from bisect import bisect_left

class Solution:
    def findPos(self, arr, element, till):
        """
        Method to find the suitable position for the current 
        index in nums, using Binary Search
        """
        index = bisect_left(arr, element, 0, till)
        return index
        
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        Method to return the longest increasing subsequence
        of an array
        """
        dp = [0] * len(nums)
        lis_len = 0
        
        for element in nums:
            
            dp_index = self.findPos(dp, element, lis_len)
            
            if dp_index == len(nums):
                continue
            
            dp[dp_index] = element
            
            if dp_index == lis_len:
                lis_len += 1
                
        return lis_len

    def test_lengthOfLIS(self):

        assert lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
        assert lengthOfLIS([0,1,0,3,2,3]) == 4

        print("Sample test cases ran successfully")
