#User function Template for python3

class Solution:
    def knapSack(self, total_capacity, weights, values, n):
        '''
        :param total_capacity: capacity of knapsack 
        :param weights: list containing weights
        :param values: list containing corresponding values
        :param n: size of lists
        :return: Integer
        '''
        # code here
        
        # create a n×total_capacity matrix, with the capacity=0 column as 0
        dp = [[0 for i in range(total_capacity+1)] for j in range(n)]
        
        for index in range(n):
            for current_capacity in range(total_capacity+1):
                
                if weights[index] > current_capacity:
                    dp[index][current_capacity] = dp[index-1][current_capacity]
                else:
                    dp[index][current_capacity] = max(
                                              # don't take the current index
                                              dp[index-1][current_capacity], 
                                              # take the current index
                                              values[index]+dp[index-1][current_capacity-weights[index]])  
                
        # the last value in the matrix hold the solution
        return dp[-1][-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends