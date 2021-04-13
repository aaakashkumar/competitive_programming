/*
Longest Alternating Subsequence (Wiggle Subsequence)
https://leetcode.com/problems/wiggle-subsequence/
@author Akash Kumar
*/

public class Solution {
    public int wiggleMaxLength(int[] nums) {
        
        if (nums.length < 2)
            return nums.length;
        
        int up = 1, down = 1;
        
        for (int i = 1; i < nums.length; ++i) {
            if (nums[i] == nums[i-1])
                continue;
            
            if (nums[i] > nums[i-1])    // up
                up = down+1;
            
            else    // down
                down = up+1;
        }
        
        return Math.max(up, down);
        
    }
}