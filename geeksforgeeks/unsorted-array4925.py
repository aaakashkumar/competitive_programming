# Element with left side smaller and right side greater
# https://practice.geeksforgeeks.org/problems/unsorted-array4925/1#
# @author Akash Kumar

#User function Template for python3

def findElement( arr, n):
    
    if n == 1:
        return arr[0]
    
    greatest_from_left = [-1] * n
    smallest_from_right = [-1] * n
    
    greatest_from_left[0] = arr[0]
    smallest_from_right[-1] = arr[-1]
    
    # create two lists
    # greatest_from_left stores the maximum values from left
    # smallest_from_left stores the minimum values from the right
    for i in range(1, n):
        if arr[i] > greatest_from_left[i-1]:
            greatest_from_left[i] = arr[i]
        else:
            greatest_from_left[i] = greatest_from_left[i-1]
        
        if arr[n-1-i] < smallest_from_right[n-i]:
            smallest_from_right[n-1-i] = arr[n-1-i]
        else:
            smallest_from_right[n-1-i] = smallest_from_right[n-i]
        
    # print(greatest_from_left)
    # print(smallest_from_right)
    
    for i in range(n):
        # if a number is both greater than all the elements
        # on its left and smaller than all the elements on
        # its right, return it
        if greatest_from_left[i] == smallest_from_right[i]:
            if i != 0 and i != n-1:
                return greatest_from_left[i]
            else:
                # the extreme ends cannot be a solution since
                # they do not have greater (or smaller) values
                if i == 0:
                    continue
                elif i == n-1:
                    break
        
    return -1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        print(findElement(a, n))

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends