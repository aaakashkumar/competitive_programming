# Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
# @author Akash Kumar

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        sum_counts = {0: 1}
        possible_subarrays_count = 0
        sum_ = 0
        
        for num in nums:
            sum_ += num
            
            # if sum-k has already occurred in the prefix sum
            # that suggests that the sum (i+1)th index and the
            # jth index is k, where i is the first index where
            # the continous sum is k and j is the second such index
            if sum_-k in sum_counts:
                possible_subarrays_count += sum_counts[sum_-k]
            
            if sum_ in sum_counts:
                sum_counts[sum_] += 1
            else:
                sum_counts[sum_] = 1
        
        
        return possible_subarrays_count

    def testSubarraySum(self):
        """
        Method to test the solution to the problem
        """
        assert self.subarraySum([1,1,1], 2) == 2
        assert self.subarraySum([1,2,3], 3) == 2
        assert self.subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7) == 4
        assert self.subarraySum([1], 0) == 0
        print("All test cases ran successfully")


Solution().testSubarraySum()