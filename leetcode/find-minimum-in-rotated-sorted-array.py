# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# @author Akash Kumar

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Method to find the minimum number in the rotated list
        :param nums: list of numbers
        """
        
        i = 0               # left index
        j = len(nums)-1     # right index
        mid = (i+j) // 2    # middle index
        minimum_number = nums[i] if nums[i] < nums[j] else nums[j]  # stores the minimum value

        # while loop inspired from Binary Search
        while i < j:
            if nums[mid] < nums[i]:
                minimum_number = nums[mid]
                j = mid
                mid = (i+j) // 2

            elif nums[j] < nums[mid]:
                minimum_number = nums[j]
                i = mid
                mid = (i+j) // 2

            else:
                break

            if j-i == 1:
                break 

        return minimum_number

    def testFindMin(self):
        """
        A method to test findMin()
        """
        assert self.findMin([3,4,5,1,2]) == 1
        assert self.findMin([4,5,6,7,0,1,2]) == 0
        assert self.findMin([11,13,15,17]) == 11
        assert self.findMin([5,6,7,8,9,10,11,1,2,3,4]) == 1
        assert self.findMin([1,2,3]) == 1

        print("All test cases ran successfully")


Solution().testFindMin()