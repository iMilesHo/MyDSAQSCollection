# 1431. Kids With the Greatest Number of Candies

## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/).


## constraints:
- length: [2,100]
- value: [1,100]
- extra: [1,50]
- return is a array of boolean value with length n

## idea:
- a nested loop to check each element
- time complexity: O(n^2)
- space complexity: O(1)

## test cases:
- [1, 1], 1 -> [True, True]
- [2,3,5,1,3], 3 -> []


## Python Solution

### My own solution

```Python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_value_without_extra = max(candies)
        for i in range(len(candies)):
            temp = extraCandies + candies[i]
            if(temp >= max_value_without_extra):
                ans.append(True)
            else:
                ans.append(False)
        return ans
```

### leetcode solution

```Python
# Fastest solution
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        max_num = max(candies)
        for i in range(len(candies)):
            ans.append(candies[i] + extraCandies >= max_num)
        return ans
```

```Python
import sys
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        for i, candy in enumerate(candies):
            greatest = (candy + extraCandies) >= maxCandies
            candies[i] = greatest
        return candies

# test code
s = Solution()
list = [2,3,5,1,3]
print(s.kidsWithCandies(list, 3)) # [True, True, True, False, True]
print(list) # [True, True, True, False, True]
```

```Python
```
