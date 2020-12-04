# https://leetcode.com/problems/counting-bits/
# @author Akash Kumar

from typing import List


class Solution:

    def countBits(self, num: int) -> List[int]:
        """
        Method to count the bits for all numbers from 0 to num
        :param num:  a non negative integer number
        :return one_counts: number of 1's in their binary representation for
        every number i in the range 0 ≤ i ≤ num
        """

        if num == 0:
            return [0]
        elif num == 1:
            return [0, 1]
        
        # bit_counts stores the final result
        one_counts = [0, 1]
        
        for i in range(2, num+1):
            if i % 2 == 0:
                one_counts.append(one_counts[i//2])
            else:
                one_counts.append(one_counts[i//2] + 1)

        # print(one_counts)
        return one_counts

    def testCountBits(self):
        """
        Method to test the solution to the problem
        """
        assert self.countBits(2) == [0,1,1]
        assert self.countBits(5) == [0,1,1,2,1,2]
        print("All test cases ran successfully")


Solution().testCountBits()