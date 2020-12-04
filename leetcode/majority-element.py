# https://leetcode.com/problems/majority-element/
# @author Akash Kumar

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Method to calculate the majority element
        :param nums: a list of integers
        """
        num_count = dict()
        nums_length = len(nums)

        for i in nums:

            if dict.get(num_count, i):
                num_count[i] += 1
            else:
                num_count[i] = 1

            if num_count[i] >= nums_length / 2:
                return i

    def majorityElementBoyerMoore(self, nums: List[int]) -> int:
        """
        Method to calculate the majority element using Boyer-Moore Voting Algorithm
        :param nums: a list of integers
        """
        current_majority = None
        majority_count = 0
        majority_target = len(nums)//2

        for i in nums:
            if majority_count == 0:
                current_majority = i

            if i == current_majority:
                majority_count += 1
            else:
                majority_count -= 1
        
        return current_majority

    def testMajorityElement(self):
        """
        A method to test majorityElement()
        """
        assert self.majorityElement([3,2,3]) == 3
        assert self.majorityElement([2,2,1,1,1,2,2]) == 2
        assert self.majorityElement([1]) == 1
        assert self.majorityElement([6,5,5]) == 5

        print("All test cases ran successfully")


Solution().testMajorityElement()