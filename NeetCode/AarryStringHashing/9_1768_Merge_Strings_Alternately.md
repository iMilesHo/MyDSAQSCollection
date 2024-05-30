#  1768. Merge Strings Alternately

## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/merge-strings-alternately/description/).


## constraints:
- word length: [1, 100]
- all of lowercase

## idea:
- declare a new string to store the merged string
- time complexity: O(n+m)
- space comlexity: O(n+m)

## test cases:

## My own solution

```Python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergedString = ""
        for i in range(min(len(word1),len(word2))):
            mergedString += word1[i]
            mergedString += word2[i]
        if len(word1) < len(word2):
            mergedString += word2[len(word1):len(word2)]
        elif len(word1) > len(word2):
            mergedString += word1[len(word2):len(word1)]
        return mergedString
```

## Notes:
- In python, String is immutable, so it is better to use list to store the merged string and then use join to convert the list to string. Basically, the String manipulation is not efficient in python compared to list manipulation.
- But the String needs less space than list. So, it is a trade-off between time and space.

## leetcode solution
```Python
# Fastest solution
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        i, j = 0, 0

        while i< len(word1) and j < len(word2):
            ans.append(word1[i])
            ans.append(word2[j])
            i +=1
            j +=1
        
        ans.append(word1[i:])
        ans.append(word2[j:])

        return ''.join(ans)
```

```Python
# Memory efficient solution 
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        res = ''
        
        for i in range(max(len(word1),len(word2))):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]

        return ''.join(res)
```


