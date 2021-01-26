# Maximum Index
# https://practice.geeksforgeeks.org/problems/maximum-index-1587115620/1
# @author Akash Kumar


#User function Template for python3

#Complete this function
def maxIndexDiff(arr, n): 
    ##Your code here
    
    descending_from_left = []	# to store the decreasing items starting from the leftmost index
    descending_from_right = []	# to store the increasing items from the rightmost index, reversed
    
    i, j = 0, n-1
    
    # create descending_from_left and descending_from_right lists
    while i < n:
        if not descending_from_left or arr[i] <= descending_from_left[-1][0]:
            descending_from_left.append((arr[i], i))
            
        if not descending_from_right or arr[j] >= descending_from_right[-1][0]:
            descending_from_right.append((arr[j], j))
        
        i += 1
        j -= 1
            
    # print(descending_from_left)
    descending_from_right.reverse()
    # print(descending_from_right)
    
    i, j, max_difference = 0, 0, 0
    while i < len(descending_from_left) and j < len(descending_from_right):
	# compare descending_from_left and descending_from_right to get the maximum difference

        if descending_from_left[i][0] <= descending_from_right[j][0]:
            if (descending_from_right[j][1] - descending_from_left[i][1]) > max_difference:
                max_difference = descending_from_right[j][1] - descending_from_left[i][1]
            j += 1
        
        else:
            i += 1
            
    return max_difference

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            print(maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
