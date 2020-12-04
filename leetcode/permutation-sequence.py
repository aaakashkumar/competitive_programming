# https://leetcode.com/problems/permutation-sequence/
# @author Akash Kumar

class Solution:
    def calculateFactorial(self, num):
        """
        Method to calculate factorial till 'num' numbers
        :param num: The number till which factorial is to be calculated
        :return factorial: A list, where each element a_i at index i, represents 
        the factorial i!
        """
        self.factorial = [1]

        for i in range(1,num+1):
            self.factorial.append(self.factorial[i-1] * i)
        
        return self.factorial

    def getPermutation(self, n: int, k: int) -> str:
        """
        Method to calculate the kth permutation, as per the problem statement
        :param n: n defines that the set of numbers will include numbers from 1 to n
        :param k: the position of the permutation that is to be found
        :return nums: the kth permutation, as a string
        """

        # hardcode self.factorial = [1,1,2,6,24,120,720,5040,40320,362880] for faster performance
        self.calculateFactorial(9)  
        
        nums = list(range(1,n+1))  # the operations will be done in place in the list
        
        index = 0
        swap_index = index+1

        while k != 0:
            # for an example number 1XXX, there can be 3! possibilities 
            # for numbers starting with 1
            possible_numbers = self.factorial[n-(index+1)]

            if possible_numbers == k:
                # for an example number 1234, if k=6, 
                # then possible numbers equals 6
                # in this case, simply traverse to the last number after 1XXX
                # which will simply be XXX in descending order, i.e., 1432
                k -= possible_numbers
                nums[index+1:] = reversed(nums[index+1:])
                break

            if possible_numbers < k:
                # for an example number 123 and k=3,
                # for numbers starting with 1, possible numbers are 2!=2
                # after traversing 2 numbers, you have to traverse k-2=1 more numbers.
                # after traversing 2 numbers, you get 2XX (obtained by swapping)
                # possible numbers for 2XX is 2! = 2
                # however, k=1 now, so the first digit will be 2
                # set the index to the next digit
                k -= possible_numbers
                # if k == 0: break
                nums[index], nums[swap_index] = nums[swap_index], nums[index]
                swap_index += 1
            
            else:
                # for an example number 1234, and k=9
                # 1XXX has 3!=6 possible numbers
                # after covering 1XXX, there are k-6=3 more numbers to traverse
                # for 2XXX, you again have 3!=6 possible numbers
                # but since k=3, the first digit will be 2
                # so move on to the next digit
                index += 1
                swap_index = index+1

        return ''.join(map(str,nums))

    def testGetPermutation(self):
        """
        A method to test getPermutation()
        """
        assert self.getPermutation(3,3) == "213"
        assert self.getPermutation(4,9) == "2314"
        assert self.getPermutation(3,1) == "123"
        assert self.getPermutation(3,2) == "132"
        
        print("All test cases ran successfully")


Solution().testGetPermutation()