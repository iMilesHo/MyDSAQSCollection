# 334. Increasing Triplet Subsequence

## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/increasing-triplet-subsequence/).

## constraints:
- length: [1, 5*10^5]
- value: [-2^31, 2^31-1]

## ideas:
- naive:
    - for each element we can find if it can be the start of a triple of indices
    - time complexity: O(n^3)
    - space complexity: O(1)
- optimised:
    

##  test cases:
- 


## Python Solution

### Python NOTES
- `float('inf')` is a good way to represent the maximum value in python
- `float('-inf')` is a good way to represent the minimum value in python

### My own solution
```Python
# Naive solution
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            left = i
            mid = left
            while mid < len(nums):
                if nums[left] >= nums[mid]:
                    mid += 1
                else:
                    right = mid
                    while right < len(nums):
                        if nums[mid] >= nums[right]:
                            right += 1
                        else:
                            if left < mid and mid < right and right < len(nums):
                                return True
        return False
```

### leetcode solution

```Python
# Optimised solution
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        min_arr = []
        for value in nums:
            if min_arr and value > min_arr[-1]:
                min_arr.append(min_arr[-1])
            else:
                min_arr.append(value)
        
        max_arr = []
        for value in nums[::-1]:
            if max_arr and value < max_arr[-1]:
                max_arr.append(max_arr[-1])
            else:
                max_arr.append(value)
        max_arr = max_arr[::-1]
        
        for i in range(len(nums)):
            if min_arr[i] < nums[i] < max_arr[i]:
                return True

        return False
```

#### Notes - Greedy thinking
- we can keep track of the first and second smallest elements, since if we the more less elements we find at the beginning, the more chance we can find the third one that is greater than the first and second smallest elements
- even the first and second smallest elements are not in the increasing order, we can keep track of the third smallest element

```Python
# more optimised solution
# Time complexity: O(n)
# Space complexity: O(1)
# greedy approach:
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        
        first = float('inf')
        second = float('inf')
        for third in nums:
            if third > second:
                return True
            if third <= first:
                first = third
            else:
                second = third
        return False
```