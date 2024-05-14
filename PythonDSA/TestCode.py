from typing import List, Optional
from traitlets import Int
from collections import Counter, defaultdict, deque

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        while len(s) > 0:
            temp = s.pop()
            length = 1

            temp1 = temp
            while temp1 + 1 in s:
                length += 1
                temp1 += 1
                s.remove(temp1)
            
            while temp - 1 in s:
                length += 1
                temp -= 1
                s.remove(temp)
                
            if length > longest:
                longest = length
        return longest
    

sol = Solution()
nums = [1, 0, -1]
print(sol.longestConsecutive(nums))