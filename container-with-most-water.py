# https://leetcode.com/problems/container-with-most-water
# @author Akash Kumar

from typing import List

class Solution:
    def smallerHeight(self, left_height, right_height):
        """
        A method that simply returns the smaller of two numbers
        :param left_height: The left height in the container
        :param right_height: The right height in the container
        :return: the smaller height between left_height and right_height
        """
        return left_height if left_height < right_height else right_height

    def maxArea(self, height: List[int]) -> int:
        """
        A method to calculate the maximum area as described in the problem statement
        :param height: A list of all the heights
        :return max_area: The maximum area possible of the container
        """
        left = 0
        right = len(height) - 1
        max_area = -1
        
        while left < right:
            new_area = (right-left) * self.smallerHeight(height[left], height[right])
            if new_area > max_area:
                max_area = new_area

            # if the left height is shorter of the two heights
            # then set the left height to the next greater left height
            if height[left] <= height[right]:
                current_left = left
                left += 1
                while height[current_left] > height[left] and left < right:
                    left += 1

            # if the right height is shorter of the two heights
            # then set the right height to the next greater right height
            elif height[right] < height[left]:
                current_right = right
                right -= 1
                while height[current_right] > height[right] and right > left:
                    right -= 1

            else:
                break
        
        return max_area

    def testMaxArea(self):
        """
        A method to test maxArea()
        """
        assert self.maxArea([1,8,6,2,5,4,8,3,7]) == 49
        assert self.maxArea([1,1]) == 1
        assert self.maxArea([4,3,2,1,4]) == 16
        assert self.maxArea([1,2,1]) == 2
        assert self.maxArea([1,3,2,5,25,24,5]) == 24
        print("All test cases ran successfully")


Solution().testMaxArea()