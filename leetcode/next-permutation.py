# Next Permutation
# https://leetcode.com/problems/next-permutation/
# @author Akash Kumar


from typing import List


class Solution:
    
    def reverse_slice(self, arr, start_index, end_index):
        while start_index < end_index:
            arr[start_index], arr[end_index] = \
                arr[end_index], arr[start_index]
            
            start_index += 1
            end_index -= 1
            
        return arr
    
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # find the index which is smaller than a decreasing sequence
        # from the right
        swap_index = len(nums) - 2
        while nums[swap_index] >= nums[swap_index+1] and swap_index >= 0:
            swap_index -= 1
        
        if swap_index == -1:
            nums = nums.reverse()
        
        elif swap_index == len(nums)-1:
            nums[len(nums)-1], nums[len(nums)-2] = \
                nums[len(nums)-2], nums[len(nums)-1]
            
        else:
            # find the number just greater than the one at swap_index
            # starting from the right
            greater_than_swap_index = len(nums) - 1
            while nums[greater_than_swap_index] <= nums[swap_index] and greater_than_swap_index > 0:
                greater_than_swap_index -= 1

            nums[swap_index], nums[greater_than_swap_index] = \
                nums[greater_than_swap_index], nums[swap_index]

            # reverse the slice that is after the swap index
            # caution: don't use list slicing due to it's additional time complexity
            self.reverse_slice(nums, swap_index+1, len(nums)-1)

    def testNextPermutation(self):
        """
        Method to test nextPermutation()
        """

        nums = [1,2,3]
        self.nextPermutation(nums)
        assert nums == [1,3,2]

        nums = [3,2,1]
        self.nextPermutation(nums)
        assert nums == [1,2,3]

        nums = [1,1,5]
        self.nextPermutation(nums)
        assert nums == [1,5,1]

        nums = [1]
        self.nextPermutation(nums)
        assert nums == [1]

        nums = [5,1,1]
        self.nextPermutation(nums)
        assert nums == [1,1,5]

        print("All sample test cases ran successfully")

Solution().testNextPermutation()