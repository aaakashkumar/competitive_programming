# https://leetcode.com/problems/4sum/
# @author Akash Kumar

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        :param nums: A list of integers
        :param target: The target to sum up to
        """

        quadruplets = list()

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                hash_ = []
                for k in range(j+1, len(nums)):
                    # print(i,j,k)

                    # check if the complement (the last number that should be added)
                    # has already been found (in the hash)
                    complement = target-(nums[i]+nums[j]+nums[k])
                    if complement in hash_:
                        # print(i,j,k,complement)

                        # sort the numbers so that they can be searched the next time to avoid duplicates
                        temp_quad = sorted([nums[i], nums[j], nums[k], complement])
                        if temp_quad not in quadruplets:
                            quadruplets.append(temp_quad)
                        
                    hash_.append(nums[k])
        
        return quadruplets

    def test_fourSum(self):
        assert sorted(self.fourSum([1,0,-1,0,-2,2], 0)) == sorted([[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
        assert self.fourSum([], 0) == []
        assert sorted(self.fourSum([-2,-1,-1,1,1,2,2], 0)) == sorted([[-2,-1,1,2],[-1,-1,1,1]])
        print("All test cases ran successfully")

Solution().test_fourSum()