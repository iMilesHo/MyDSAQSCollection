# 125. Valid Palindrome

## file name: 30_125_valid_palindrome.md

## constraits:
- length: [1, 2*10^5]

## ideas:
- we just use two pointors to go through the string forward and backword
 - for every character we convert it to lowercase and if we meet a non-alphanumic characters we just skip it

## Python Solution

### My Solution
```python
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
                if left >= right:
                    break
            while left < right and not s[right].isalnum():
                right -= 1
                if left >= right:
                    break

        return True
```

### Leetcode Solution
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:            
        left, right = 0, len(s)-1
        s = s.lower()

        while left<right:
            while left<right and not s[left].isalnum():
                left += 1
            
            while left<right and not s[right].isalnum():
                right -= 1

            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
```

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        ans = ""
        s = s.lower()
        for letter in s:
            if letter.isalnum():
                ans+= letter
        return ans == ans[::-1]             
```


