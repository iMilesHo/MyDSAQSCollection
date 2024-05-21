from typing import List, Optional
from traitlets import Int
from collections import Counter, defaultdict, deque

# 76. Minimum Window Substring

# Given two strings s and t of lengths m and n respectively, return the minimum window 
# substring
#  of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

class Solution:
    def isMet(self, t: str, s: str) -> bool:
        t_c = Counter(t)
        s_c = Counter(s)
        for k, v in t_c.items():
            if s_c[k] < v:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        if not self.isMet(t, s):
            return ""
        min_ans = s
        def helper(s1):
            nonlocal min_ans
            if len(min_ans) > len(s1):
                min_ans = s1
            
            left = right = s1
            if len(s1[1:]) >= len(t) and self.isMet(t, s1[1:]):
                left = helper(s1[1:])
            if len(s1[:-1]) >= len(t) and self.isMet(t, s1[:-1]):
                right = helper(s1[:-1])
            
            ans = s1
            if left and left < ans:
                ans = left
            if right and right < ans:
                ans = right
            return ans
        helper(s)
        return min_ans
        
# test
s = "acbbaca"
t = "aba"
sol = Solution()
print(sol.minWindow(s, t)) # "BANC"