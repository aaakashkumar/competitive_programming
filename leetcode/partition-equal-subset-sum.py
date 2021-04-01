# Partition Equal Subset Sum
# https://leetcode.com/problems/partition-equal-subset-sum/
# @author Akash Kumar
# read — https://www.educative.io/courses/grokking-dynamic-programming-patterns-for-coding-interviews/3jEPRo5PDvx


class Solution(object):
    def canPartition(self, nums):
        """
        Recursive DP solution for checking if an array and be partitioned into
        equal sum sets
        :type nums: List[int]
        :rtype: bool
        """
        
        sum_ = sum(nums)
        
        # if the sum is not even, there can't be two subsets
        if sum_ % 2 != 0:
            return False
        
        # the total that one subset has to make
        sum_ = int(sum_/2)
        
        dp = [[None for i in range(sum_+1)] for j in range(len(nums))]
        
        def canPartitionSubproblem(nums, sum_, index):
            nonlocal dp
            
            if sum_ == 0:
                return True
            
            if sum_ < 0 or index >= len(nums):
                return False
            
            if dp[index][sum_] is None:
                if nums[index] <= sum_:
                    can_partition_taking_current = canPartitionSubproblem(nums, sum_-nums[index], index+1)
                    if can_partition_taking_current:
                        return True
                    dp[index][sum_] = can_partition_taking_current
                
                dp[index][sum_] = canPartitionSubproblem(nums, sum_, index+1)
            
            return dp[index][sum_]
        
        return True if canPartitionSubproblem(nums, sum_, 0) else False

    def test_canPartition(self):
        """
        Method to test the canPartition() method
        """

        assert self.canPartition([1, 2, 3, 4]) == True
        assert self.canPartition([1, 1, 3, 4, 7]) == True
        assert self.canPartition([2, 3, 4, 6]) == False
        assert self.canPartition([1,5,11,5]) == True
        assert self.canPartition([1,2,3,5]) == False
        assert self.canPartition([100]*198 + [99, 97]) == False

        print("Sample test cases ran successfully")

Solution().test_canPartition()