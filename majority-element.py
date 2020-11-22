# https://leetcode.com/problems/majority-element/
# @author Akash Kumar

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Method to calculate the majority element
        :param nums: a list of integers
        """
        nums = sorted(nums)
        nums_length = len(nums)

        count = 1
        i_previous = None
        for i in nums:
            if count >= nums_length / 2:
                return i
            
            if i != i_previous:
                count = 1

            count += 1
            i_previous = i

    def testMajorityElement(self):
        """
        A method to test majorityElement()
        """
        assert self.majorityElement([3,2,3]) == 3
        assert self.majorityElement([2,2,1,1,1,2,2]) == 2
        assert self.majorityElement([1]) == 1

        print("All test cases ran successfully")


Solution().testMajorityElement()