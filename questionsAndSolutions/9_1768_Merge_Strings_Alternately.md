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

### leetcode solution
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


