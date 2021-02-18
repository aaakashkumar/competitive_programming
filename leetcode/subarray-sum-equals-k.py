# Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
# @author Akash Kumar

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        possible_subarray_count = 0
        
        for i in range(len(nums)):
            subarray_sum = 0
            for j in range(i, len(nums)):
                subarray_sum += nums[j]
                
                if subarray_sum == k:
                    possible_subarray_count += 1
        
        return possible_subarray_count
