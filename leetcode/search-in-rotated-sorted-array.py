# https://leetcode.com/problems/search-in-rotated-sorted-array/
# @author Akash Kumar

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        """

        if len(nums) == 1:
            return 0 if nums[0] == target else -1

        left = 0
        right = len(nums) - 1
        # mid = (left+right) // 2

        while left <= right:
            mid = (left + right) // 2

            print(left, mid, right)
            if nums[mid] == target:
                return mid

            if abs(mid-left) == 1 or abs(right-mid) == 1:
                if nums[left] == target: return left
                elif nums[right] == target: return right
                elif nums[mid] == target: return mid

            if nums[left] < nums[mid-1]:
                if target >= nums[left] and target <= nums[mid-1]:
                    right = mid-1
                    continue

            if nums[left] > nums[mid-1]:
                if target >= nums[left] or target <= nums[mid-1]:
                    right = mid-1
                    continue
            
            if nums[mid+1] < nums[right]:
                if target >= nums[mid+1] and target <= nums[right]:
                    left = mid+1
                    continue

            if nums[mid+1] > nums[right]:
                if target >= nums[mid+1] or target <= nums[right]:
                    left = mid+1
                    continue

            return -1

        return -1

    def testSearch(self):
        """
        """
        
        assert self.search([4,5,6,7,0,1,2], 0) == 4
        assert self.search([4,5,6,7,0,1,2], 3) == -1
        assert self.search([1], 0) == -1
        assert self.search([1,3], 3) == 1
        assert self.search([1,3], 2) == -1
        assert self.search([5,1,3], 5) == 0
        assert self.search([3,4,5,6,1,2], 2) == 5
        assert self.search([6,1,2,3,4,5], 1) == 1
        assert self.search([5,1,2,3,4], 4) == 4
        assert self.search([8,1,2,3,4,5,6,7], 6) == 6

        print("All sample test cases ran successfully")

Solution().testSearch()