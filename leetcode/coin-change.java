class Solution {
    public int coinChange(int[] coins, int amount) {
        double[][] dp = new double[coins.length+1][amount+1];
        
        for (int i = 0; i < coins.length+1; ++i) 
            dp[i][0] = 0;
        
        for (int j = 1; j < amount+1; ++j) 
            dp[0][j] = Double.POSITIVE_INFINITY;
        
        for (int i = 1; i <= coins.length; ++i) {
            for (int j = 1; j <= amount; ++j) {
                if (coins[i-1] > j)
                    dp[i][j] = dp[i-1][j];
                else
                    dp[i][j] = Math.min(dp[i-1][j], 1+dp[i][j-coins[i-1]]);
            }
        }
        return (dp[coins.length][amount] != Double.POSITIVE_INFINITY) ? (int)(dp[coins.length][amount]) : -1;
    }
}