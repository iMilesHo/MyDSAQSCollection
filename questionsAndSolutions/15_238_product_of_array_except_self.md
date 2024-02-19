# 238. Product of Array Except Self
## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/reverse-words-in-a-string/description/).


## constraints:
- length: [2, 10^5]
- value: [-30, 30]
- product can be stored in a 32-bit integer
- time complexity should be O(n) without using the division operation

## ideas:
- use the prefix and postfix stratege
- in one loop, for each step, we can confirm its prefix product
- and we can go though the loop in a reverse direction at the same time
```
[1,2,3,4,5,6,7]

ans[1,1,1,1,1,1,1]
prefix_product:1
postfix_product:1

ans[1,1,1,1,1,1,1]
prefix_product:1*1
postfix_product:1*7

ans[1,1*1,1,1,1,1*7,1]
prefix_product:1*1*2
postfix_product:1*7*6

ans[1,1*1,2*1,1,1*7*6,1*7,1]
prefix_product:1*1*2*3
postfix_product:1*7*6*5
```

## test case:
- [1,2,3,4,5]


## Python Solution

### My own solution

```Python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        prefix_product = 1
        postfix_product = 1
        for i in range(len(nums)):
            ans[i] *= prefix_product
            prefix_product *= nums[i]
            ans[len(nums)-1-i] *= postfix_product
            postfix_product *= nums[len(nums)-1-i]
        return ans         
```