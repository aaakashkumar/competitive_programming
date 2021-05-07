// Poor Pigs
// https://leetcode.com/problems/poor-pigs/
// @author Akash Kumar

class Solution {
    public int poorPigs(int buckets, int minutesToDie, int minutesToTest) {
        return (int) Math.ceil(Math.log(buckets) / 
                               Math.log((int) minutesToTest/minutesToDie+1));
    }

    public static void main(String[] args) {
        Solution test = new Solution();

        assert test.poorPigs(1000, 15, 60) == 5;
        assert test.poorPigs(4, 15, 15) == 2;
        assert test.poorPigs(4, 15, 30) == 2;
        System.out.println("Sample cases executed successfully");
    }
}