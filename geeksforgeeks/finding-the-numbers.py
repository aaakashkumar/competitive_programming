# Finding the numbers
# https://practice.geeksforgeeks.org/problems/finding-the-numbers0215/1
# @author Akash Kumar


#User function Template for python3

class Solution:
    # (explanation at bottom)
    
	def singleNumber(self, nums):
		
		xor_sum = 0
		# xor  all the numbers in the list
		for number in nums:
		    xor_sum ^= number
		    
        # first_number and second_number will store the two unique numbers
		first_number = 0
		second_number = 0
		
        # get the rightmost bit that is 1, in the above xor result
		rightmost_set_bit = xor_sum & -xor_sum
		
        # divide the main array into two arrays based on whether the bit
        # at the same position as rightmost_set_bit's set bit is 1 or 0
        # and xor the two different lists
		for number in nums:
		    if number & rightmost_set_bit == 0:
		        first_number ^= number
		    
		    elif number & rightmost_set_bit > 0:
		        second_number ^= number
		        
		return min(first_number, second_number), max(first_number, second_number)



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends



"""
# Explanation
> the following is written in markdown

```python
[1, 2, 3, 2, 1, 4]
```

in binary,

01, 10, 11, 10, 01, 100

xor all the numbers:

1^2^3^2^1^4 = 7, ..., that is, 111

> - the duplicate elements will cancel out (1^1 = 0, 2^2 = 0)
> -  and what will be left is the xor of the two unique elements (111 in this case)

> only a number xorred with itself can produce a 0. so, the result obtained in the above step (xor between two different numbers) will always have atleast one set bit (1) in the result.

choose one of these set bits (easy to get the rightmost set bit),

> to ge the rightmost bit of x = 2, AND x with it's 2's Compliment

and divide the list in two, based on whether the numbers have a set bit in the position same as above (in this case, at the 0th place from right):

[01, 11, 01], [10, 10, 100]

```python
[1, 2, 3, 2, 1, 4]
```

"""