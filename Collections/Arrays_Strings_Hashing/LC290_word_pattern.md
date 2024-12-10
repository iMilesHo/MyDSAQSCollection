# 290. Word Pattern

## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/word-pattern/description/).


## Constraints:

- 1 <= pattern.length <= 300
- pattern contains only lower-case English letters.
- 1 <= s.length <= 3000
- s contains only lowercase English letters and spaces ' '.
- s does not contain any leading or trailing spaces.
- All the words in s are separated by a single space.
- return false or true

##  basic idea:
- judge if the number of elements in this two string are the same
    - if not, then return false
    - if yes, then move on to the next step
- 2nd step:
abba dog cat cat dog
^     ^
abba dog cat cat dog
   ^              ^

- Time complxity is O(n^2)
- Space complxity is O(1)

## Test cases
Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false

## My own solution
```Python
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(s_list) != len(pattern):
            return False
        for i in range(len(pattern)):
            pattern_temp = pattern[i]
            s_temp = s_list[i]
            for j in range(i, len(pattern)):
                if pattern_temp == pattern[j] and s_temp!=s_list[j]:
                    return False
                elif pattern_temp != pattern[j] and s_temp==s_list[j]:
                    return False
                    
        return True
# Time complexity: O(n^2)
# Space complexity: O(1)
```








