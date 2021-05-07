# Poor Pigs
# https://leetcode.com/problems/poor-pigs/
# @author Akash Kumar

import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return math.ceil(math.log(buckets, minutesToTest/minutesToDie + 1))

    def testPoorPigs(self):
        assert self.poorPigs(1000, 15, 60) == 5
        assert self.poorPigs(4, 15, 15) == 2
        assert self.poorPigs(4, 15, 30) == 2

        print("Sample cases executed successfully")

Solution().testPoorPigs()