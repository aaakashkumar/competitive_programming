# https://leetcode.com/problems/permutation-sequence/
# @author Akash Kumar

class Solution:
    def calculateFactorial(self, num):
        self.factorial = [1]

        for i in range(1,num+1):
            self.factorial.append(self.factorial[i-1] * i)
        
        return self.factorial

    def getPermutation(self, n: int, k: int) -> str:
        # hardcode self.factorial = [1,1,2,6,24,120,720,5040,40320,362880] for faster performance
        self.calculateFactorial(9)  
        
        nums = list(range(1,n+1))
        
        index = 0
        swap_index = index+1

        while k != 0:
            possible_numbers = self.factorial[n-(index+1)]

            if possible_numbers == k:
                k -= possible_numbers
                nums[index+1:] = reversed(nums[index+1:])
                break

            if possible_numbers < k:
                k -= possible_numbers
                nums[index], nums[swap_index] = nums[swap_index], nums[index]
                swap_index += 1
            
            else:
                index += 1
                swap_index = index+1

        return ''.join(map(str,nums))

    def testGetPermutation(self):
        assert self.getPermutation(3,3) == "213"
        assert self.getPermutation(4,9) == "2314"
        assert self.getPermutation(3,1) == "123"
        assert self.getPermutation(3,2) == "132"
        
        print("All test cases ran successfully")


Solution().testGetPermutation()