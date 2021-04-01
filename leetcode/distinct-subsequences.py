# Distinct Subsequences
# https://leetcode.com/problems/distinct-subsequences/
# @author Akash Kumar


class Solution(object):
    def numDistinct(self, s, t):
        """
        See https://www.geeksforgeeks.org/ways-transforming-one-string-removing-0-characters/
        :type s: str
        :type t: str
        :rtype: int
        """
        
        dp = [[0 for i in range(len(s))] for j in range(len(t))]
        
        dp[0][0] = 1 if s[0] == t[0] else 0
        
        for i in range(len(t)):
            for j in range(i, len(s)):
                if i == 0:
                    if j > 0:
                        dp[i][j] = 1+dp[i][j-1] if t[i] == s[j] else dp[i][j-1]
                
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1] if t[i] == s[j] else dp[i][j-1]
         
        # from pprint import pprint
        # pprint(dp)
                    
        return dp[-1][-1]
    
    def test_numDistinct(self):
        """
        Method to test the solution
        """

        assert self.numDistinct("rabbbit", "rabbit") == 3
        assert self.numDistinct("ddd", "dd") == 3
        assert self.numDistinct("abcccdf", "abccdf") == 3

        print("Sample test cases ran successfully")

Solution().test_numDistinct()