# 151. Reverse Words in a String
## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/reverse-words-in-a-string/description/).


## constraints:
- lenght of the string: 1 <= s.length <= 10^4
- s contains English letters, digits, and spaces ' '
- at least one word in the string

## ideas:
- using split to convert the string to list
- reverse
- ' '.join()
- time complexity: O(n)
- space complxity: O(n)

## test case:
- 


## Python Solution

### My own solution

```Python
class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split()
        list_s.reverse()
        return " ".join(list_s)
```

### leetcode solution

```Python
class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        return " ".join(x[::-1])
```
