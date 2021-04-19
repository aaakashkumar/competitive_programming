// Pairs of Songs With Total Durations Divisible by 60
// https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
// @author Akash Kumar

class Solution {
    public int numPairsDivisibleBy60(int[] time) {
        int[] remainders = new int[60];
        
        for (int element: time)
            remainders[element%60]++;
        
        int pairsCount = 0;
        
        pairsCount += remainders[0] * (remainders[0]-1) / 2;
        
        for (int i=1; i<60 && i!=(60-i) ; ++i)
            pairsCount += remainders[i] * remainders[60-i];
        
        pairsCount += remainders[30] * (remainders[30]-1) / 2;
        
        return pairsCount;
    }
}