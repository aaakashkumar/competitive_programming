# Subarray Sums Divisible by K
# https://leetcode.com/problems/subarray-sums-divisible-by-k
# Explanation: https://github.com/aaakashkumar/competitive_programming/blob/main/leetcode/subarray-sums-divisible-by-k.md
# @author Akash Kumar


from typing import List

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        prefix_sum = [0]
        for index in range(len(A)):
            prefix_sum.append(prefix_sum[index] + A[index])
        
        remainder_counts = dict()
        for sum_ in prefix_sum:
            if sum_ % K in remainder_counts:
                remainder_counts[sum_ % K] += 1
            else:
                remainder_counts[sum_ % K] = 1
                
        # print(prefix_sum)
        # print(remainder_counts)
        
        possible_subarrays = 0
        for remainder in remainder_counts.values():
            possible_subarrays += remainder * (remainder-1) // 2
                
        return possible_subarrays
        
# for testing
# print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5))