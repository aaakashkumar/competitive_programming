# https://leetcode.com/problems/3sum-closest/
# @author Akash Kumar

from enum import Enum
from tqdm import tqdm

class MAGIC_NUMBERS(Enum):
    NO_INDICES_LEFT = 1

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
    def get_min_sum_recursively(self, arr, target, total=0, index=0, number_count=0):
        """
        :param arr: array of integers 
        :param target: the target value, with which the 3Sum difference should be the lowest
        :param index: current index 
        :param number_count: number of elements summed
        :return: value of the current minimum sum
        """

        if number_count == 3:
            return total

        if index > len(arr)-1 and number_count < 3:
            return MAGIC_NUMBERS.NO_INDICES_LEFT

        take_this = self.get_min_sum_recursively(arr, target, total=total+arr[index], index=index+1, number_count=number_count+1)

        dont_take_this = self.get_min_sum_recursively(arr, target, total=total, index=index+1, number_count=number_count)

        if dont_take_this == MAGIC_NUMBERS.NO_INDICES_LEFT and take_this != MAGIC_NUMBERS.NO_INDICES_LEFT:
            return take_this

        if take_this == MAGIC_NUMBERS.NO_INDICES_LEFT and dont_take_this != MAGIC_NUMBERS.NO_INDICES_LEFT:
            return dont_take_this

        if take_this == MAGIC_NUMBERS.NO_INDICES_LEFT and dont_take_this == MAGIC_NUMBERS.NO_INDICES_LEFT:
            return MAGIC_NUMBERS.NO_INDICES_LEFT

        if abs(target-take_this) < abs(target-dont_take_this):
            return take_this
        else:
            return dont_take_this

    def get_min_sum(self, arr, target):
        """
        :param nums: array of integers 
        :param target: the target value, with which the 3Sum difference should be the lowest
        :return:
        """

        arr = sorted(arr)
        minimum_diff = float('inf') 
        minimum_sum = None

        for i in tqdm(range(0, len(arr)-1-1)):
            # fix one index (i), and take sum of the rest of the array using two-pointers

            left = i + 1
            right = len(arr)-1

            while left < right:
                current_sum = arr[i] + arr[left] + arr[right]
                
                if current_sum == target:
                    return current_sum
                
                diff = abs(target - (current_sum))
                if diff < minimum_diff: 
                    minimum_diff = diff
                    minimum_sum = current_sum

                if current_sum  <= target:
                    left += 1

                elif current_sum > target:
                    right -= 1

        return minimum_sum

    def test_recursive(self):
        assert self.get_min_sum_recursively([-1,2,1,-4], 1) == 2
        assert self.get_min_sum_recursively([0,0,0], 1) == 0
        assert self.get_min_sum_recursively([1,1,1,1], 0) == 3
        assert self.get_min_sum([4,-8,98,-51,73,12,-31,39,87,-16,20,69,18,59,54,44,-58,40,-36,22,-60,-8,-43,83,88,1,-25,71,-53,33,60,32,61,-5,28,38,-28,45,25,-68,-60,-87,5,-94,-19,-31,-35,-29,0,24,-62,-84,-7,-94,-89,12,97,-32,-89,92,-50,-54,-18,12,84,-81,-99,67,24,-4,-88,61,48,-17,-17,-44,65,-18,-47,68,0,-7,78,36,0,-15,23,-4,1,-74,-64,-53,-82,-10,34,-57,-93,65,-3,-73,-8,-59,96,35,51,49,92,-8,-4,-100,-64,5,-86,-26,71,60,-85,-42,-13,-10,17,-11,59,-14,-5,34,-36,24,9,78,48,24,-88,-46,-76,31,-47,-68,29,34,-97,-69,-41,-87,-42,96,0,-90,51,-55,57,86,-61,41,1,-90,-9,63,84,-32,80,-15,-12,0,72,-22,-6,-64,94,23,-80,-25,-37,-38,69,12,-64,-95,-65,5,15,-31,-68,-55,-100,-89,-24,-66,33,-14,-40,-50,-19,-79,-4],-76) == -76 

        print("Successful")

    def test_two_pointer(self):
        assert self.get_min_sum([-1,2,1,-4], 1) == 2
        assert self.get_min_sum([0,0,0], 1) == 0
        assert self.get_min_sum([1,1,1,1], 0) == 3
        assert self.get_min_sum([0,1,2], 3) == 3
        assert self.get_min_sum([4,-8,98,-51,73,12,-31,39,87,-16,20,69,18,59,54,44,-58,40,-36,22,-60,-8,-43,83,88,1,-25,71,-53,33,60,32,61,-5,28,38,-28,45,25,-68,-60,-87,5,-94,-19,-31,-35,-29,0,24,-62,-84,-7,-94,-89,12,97,-32,-89,92,-50,-54,-18,12,84,-81,-99,67,24,-4,-88,61,48,-17,-17,-44,65,-18,-47,68,0,-7,78,36,0,-15,23,-4,1,-74,-64,-53,-82,-10,34,-57,-93,65,-3,-73,-8,-59,96,35,51,49,92,-8,-4,-100,-64,5,-86,-26,71,60,-85,-42,-13,-10,17,-11,59,-14,-5,34,-36,24,9,78,48,24,-88,-46,-76,31,-47,-68,29,34,-97,-69,-41,-87,-42,96,0,-90,51,-55,57,86,-61,41,1,-90,-9,63,84,-32,80,-15,-12,0,72,-22,-6,-64,94,23,-80,-25,-37,-38,69,12,-64,-95,-65,5,15,-31,-68,-55,-100,-89,-24,-66,33,-14,-40,-50,-19,-79,-4],-76) == -76 

        print("Successful")


# print('Testing recursive solution')
# Solution().test_recursive()
print('Testing two pointer solution')
Solution().test_two_pointer()