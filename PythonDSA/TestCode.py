from typing import List

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() == s[right].lower():
                    left += 1
                    right -= 1
                    continue
                else:
                    return False
            while not s[left].isalnum():
                left += 1
            while not s[right].isalnum():
                right -= 1

        return True
    
#test 
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))