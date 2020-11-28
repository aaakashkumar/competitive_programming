# https://leetcode.com/problems/counting-bits/
# @author Akash Kumar

from typing import List


class Solution:
    def get_number_of_ones(self, num):
        """
        Method to get the number of ones in the binary representation of num
        :param num: An integer
        :return number_of_ones: The number of ones in the binary representation of num
        """
        number_of_ones = 0
        while num > 0:
            if num % 2 == 1:
                number_of_ones += 1
            num //= 2
        return number_of_ones

    def get_powers_of_two(self):
        """
        Generator to generate the powers of 2, starting from 2^1
        """
        exponent = 1
        value = 2
        while True:
            yield value
            exponent += 1
            value = 2**exponent

    def countBits(self, num: int) -> List[int]:
        """
        Method to count the bits for all numbers from 0 to num
        :param num:  a non negative integer number
        :return one_counts: number of 1's in their binary representation for
        every number i in the range 0 ≤ i ≤ num
        """

        # stores the count of 1s in the binary representations of every number after 2^n where 0≤n≤∞
        # for example, number of 1s in binary form of 2^5 and 2^78 are the same, i.e., 1
        # and also 2^5+10 and 2^78+10 will be the same
        known_one_counts = [0, 1]
        
        # bit_counts stores the final result
        one_counts = [0]

        power_of_two = self.get_powers_of_two()

        next_target = next(power_of_two)  # initially set to 2
        current_power_of_two = 1

        i = 1
        while i <= num:
            if i == next_target:
                # if i equals to any of the powers 2^n where n is a non negative integer
                # then the number of bits will be 1
                current_power_of_two = next_target
                next_target = next(power_of_two)

                if i+len(known_one_counts)-1 <= num:
                    one_counts += known_one_counts[1:]
                    i += len(known_one_counts)-1
                    continue

            if i - current_power_of_two+1 <= len(known_one_counts)-1:
                one_counts.append(known_one_counts[i-current_power_of_two+1])
            
            else:
                number_of_ones = self.get_number_of_ones(i)
                one_counts.append(number_of_ones)
                known_one_counts.append(number_of_ones)

            i += 1
        
        # print(one_counts)            
        return one_counts

    def testCountBits(self):
        """
        Method to test the solution to the problem
        """
        assert self.countBits(2) == [0,1,1]
        assert self.countBits(5) == [0,1,1,2,1,2]
        print("All test cases ran successfully")

    def test_powers_of_two(self):
        """
        Method to test the utility method, get_powers_of_two()
        """
        z = self.get_powers_of_two()
        for i in [2,4,8,16,32,64,128,256,512,1024,2048]:
            assert i == next(z)
        print("The powers returned by get_powers_of_two() are correct")


# Solution().test_powers_of_two()
Solution().testCountBits()