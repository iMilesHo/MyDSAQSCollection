# 485. Max Consecutive Ones

## complexity: Easy

## Description

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.

## Solution

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l = -1
        res = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                l = -1
            if l == -1 and nums[r] == 1:
                l = r
            if nums[r] == 1:
                res = max(r-l+1,res)
        return res
```

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1
            else:
                res = max(count, res)
                count = 0
        res = max(count, res)
        return res
```
