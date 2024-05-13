from typing import List, Optional
from traitlets import Int
from collections import Counter, defaultdict

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for center_index in range(len(s)):
            start = end = center_index
            while start >= 0 and end <= len(s):
                temp = s[start:end]
                if temp == temp[::-1] and len(temp) > len(ans):
                    ans = temp
                start -= 1
                end += 1
        return ans

# Test
s = Solution()
print(s.longestPalindrome("babad")) # "bab" or "aba"