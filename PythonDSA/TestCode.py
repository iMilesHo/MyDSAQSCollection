import sys
from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')
        for third in nums:
            if third > second:
                return True
            if third <= first:
                first = third
            else:
                second = third
        return False     

# test code
s = Solution()
list = [0,1,3]
print(s.increasingTriplet(list))

list = [1,2,3,4,5]
print(s.increasingTriplet(list))

list = [5,4,3,2,1]
print(s.increasingTriplet(list))

list = [2,1,5,0,4,6]
print(s.increasingTriplet(list))