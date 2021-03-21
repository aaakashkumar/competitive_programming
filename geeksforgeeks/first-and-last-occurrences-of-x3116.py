# First and last occurrences of x 
# https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1#
# @author Akash Kumar

#User function Template for python3

def find_first_index(arr, n, x):
    beginning = 0
    end = n-1
    
    while end >= beginning:
        middle = beginning + (end-beginning) // 2
        
        if arr[middle] == x and (middle == 0 or arr[middle-1] != x):
                return middle
        
        else:
            if arr[middle] < x:
                beginning = middle+1
            else:
                end = middle-1
                
    return -1
            

def find_last_index(arr, n, x):
    beginning = 0
    end = n-1
    
    while end >= beginning:
        middle = beginning + (end-beginning) // 2
        
        if arr[middle] == x and (middle == n-1 or arr[middle+1] != x):
            return middle
        
        else:
            if arr[middle] > x:
                end = middle-1
            else:
                beginning = middle+1
                
    return -1

def find(arr,n,x):
    return find_first_index(arr, n, x), find_last_index(arr, n, x)

#User function Template for python3

def find_first_index(arr, n, x):
    beginning = 0
    end = n-1
    
    while end >= beginning:
        middle = beginning + (end-beginning) // 2
        
        if arr[middle] == x and (middle == 0 or arr[middle-1] != x):
                return middle
        
        else:
            if arr[middle] < x:
                beginning = middle+1
            else:
                end = middle-1
                
    return -1
            

def find_last_index(arr, n, x):
    beginning = 0
    end = n-1
    
    while end >= beginning:
        middle = beginning + (end-beginning) // 2
        
        if arr[middle] == x and (middle == n-1 or arr[middle+1] != x):
            return middle
        
        else:
            if arr[middle] > x:
                end = middle-1
            else:
                beginning = middle+1
                
    return -1

def find(arr,n,x):
    return find_first_index(arr, n, x), find_last_index(arr, n, x)

#User function Template for python3

def find_first_index(arr, n, x):
    beginning = 0
    end = n-1
    
    while end >= beginning:
        middle = beginning + (end-beginning) // 2
        
        if arr[middle] == x and (middle == 0 or arr[middle-1] != x):
                return middle
        
        else:
            if arr[middle] < x:
                beginning = middle+1
            else:
                end = middle-1
                
    return -1
            

def find_last_index(arr, n, x):
    beginning = 0
    end = n-1
    
    while end >= beginning:
        middle = beginning + (end-beginning) // 2
        
        if arr[middle] == x and (middle == n-1 or arr[middle+1] != x):
            return middle
        
        else:
            if arr[middle] > x:
                end = middle-1
            else:
                beginning = middle+1
                
    return -1

def find(arr,n,x):
    return find_first_index(arr, n, x), find_last_index(arr, n, x)

#{ 
#  Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ans=find(arr,n,x)
    print(*ans)
# } Driver Code Ends