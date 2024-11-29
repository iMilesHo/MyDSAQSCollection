# 345. Reverse Vowels of a String
## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/reverse-vowels-of-a-string/description/).


## constraints:
- length: [1, 3*10^5]
- s consist of printable ASSCII

## idea:
- list(s)
- set(['a', 'e', 'i', 'o', 'u'])
- two pointer: far left, far right.
- if we encounter two vowels character we exchange them until far_left >= far_right
- time complexity: O(n)
- space complexity: O(n)

## test cases:

## Python Solution

### My own solution

```Python
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        far_left = 0
        far_right = len(s) - 1
        while far_left < far_right:
            if s[far_left] in vowels and s[far_right] in vowels:
                temp = s[far_right]
                s[far_right] = s[far_left]
                s[far_left] = temp
                far_left += 1
                far_right -= 1
            if s[far_left] not in vowels:
                far_left += 1
            if s[far_right] not in vowels:
                far_right -= 1
        return "".join(s)
```

### leetcode solution

```Python
# Fastest solution
class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        n=len(s)
        left=0
        right=n-1
        vowels=set('AEIOUaeiou')
        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
            while left<right and s[right] not in vowels:
                right-=1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        s=''.join(s)
        return s
```

```python
# Approach 2
class Solution:
    def reverseVowels(self, s: str) -> str:
        indices = []
        vowels = []
        for i, cur_s in enumerate(list(s)):
            if cur_s in 'aeiouAEIOU':
                indices.append(i)
                vowels.append(cur_s)

        s = list(s)
        for index, vowel in zip(indices[::-1], vowels):
            s[index] = vowel
        return ''.join(s)
```

