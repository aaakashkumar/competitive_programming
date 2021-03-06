# https://leetcode.com/problems/4sum/
# @author Akash Kumar

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        :param nums: A list of integers
        :param target: The target to sum up to
        """

        if nums == []: return []

        quadruplets = list()
        nums = sorted(nums)

        for i in range(len(nums)-3):
            if i>0 and nums[i] == nums[i-1]: continue
            for j in range(i+1, len(nums)-2):

                hash_ = []
                for k in range(j+1, len(nums)):
                    complement = target-(nums[i]+nums[j]+nums[k])

                    # check if the complement (the last number that should be added)
                    # has already been found (in the hash)
                    if complement in hash_:
                        # print(i,j,k,complement)
                        if [nums[i], nums[j], nums[k], complement] not in quadruplets:
                            quadruplets.append([nums[i], nums[j], nums[k], complement])
                        
                    hash_.append(nums[k])
        
        return quadruplets

    def test_fourSum(self):
        """
        Method to test the code with a few sample cases
        """
        def inner_sort(arr):
            return sorted([sorted(x) for x in arr])

        assert inner_sort(self.fourSum([1,0,-1,0,-2,2], 0)) == inner_sort([[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
        assert self.fourSum([], 0) == []
        assert inner_sort(self.fourSum([-2,-1,-1,1,1,2,2], 0)) == inner_sort([[-2,-1,1,2],[-1,-1,1,1]])
        assert self.fourSum([0,0,0,0], 0) == [[0,0,0,0]]
        assert inner_sort(self.fourSum([-5,5,4,-3,0,0,4,-2], 4)) == inner_sort([[-5,0,4,5],[-3,-2,4,5]])
        print("All test cases ran successfully")

Solution().test_fourSum()