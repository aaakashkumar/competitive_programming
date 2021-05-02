// Squares of a Sorted Array
// https://leetcode.com/problems/squares-of-a-sorted-array/
// @author Akash Kumar


class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] squares = new int[nums.length];
        
        // case 1: the entire array is positive
        if(nums[0] >= 0) {
            for(int i=0; i<nums.length; ++i) {
                squares[i] = nums[i]*nums[i];
            }
            
            return squares;
        }
        
        else {
            int firstPositive = -1;
            for(int i=0; i<nums.length; ++i) {
                // try to find the first positive number
                if (nums[i] >= 0) {
                    firstPositive = i;
                    break;
                }
            }
            
            // if the array contains both positive and negatives, use
            // 2 pointers
            if(firstPositive != -1) {
                int negativeIndex = firstPositive-1, positiveIndex = firstPositive;
                
                int currentIndex = 0;
                while(currentIndex < nums.length) {
                    if (negativeIndex < 0)
                        squares[currentIndex++] = (int) Math.pow(nums[positiveIndex++], 
                                                                 2);
                    else if(positiveIndex >= nums.length)
                        squares[currentIndex++] = (int) Math.pow(nums[negativeIndex--],
                                                                 2);
                    else if (-nums[negativeIndex] < nums[positiveIndex])
                        squares[currentIndex++] = (int) Math.pow(nums[negativeIndex--],
                                                                 2);
                    else
                        squares[currentIndex++] = (int) Math.pow(nums[positiveIndex++],
                                                                 2);
                }
            }
            
            // in case all elements are negative
            else {
                for(int i=nums.length-1; i>=0; --i)
                    squares[nums.length-1-i] = (int) Math.pow(nums[i], 2);
            }
            
            return squares;
        }
    }
}