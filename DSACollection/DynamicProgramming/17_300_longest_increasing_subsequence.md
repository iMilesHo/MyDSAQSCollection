# 300. longest increasing subsequence

## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/longest-increasing-subsequence/).

## constraints:
- length: [1,2500]
- value: [-10^4, 10^4]

## ideas:
10,9,2,5,3,7,101,18


## test cases:

## Python Solution

### Naive solution
- time complexity: O(2^n)
- space complexity: O(n)

```Python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Function to find the length of LIS ending with the last element included
        def findLIS(index, prev):
            # Base case: If we've processed all elements
            if index == len(nums):
                return 0
            
            # Case 1: Exclude the current element and move to the next element
            taken = 0
            if nums[index] > prev:
                # Case 2: Include the current element if it is greater than the previous element in the LIS
                taken = 1 + findLIS(index + 1, nums[index])
            
            not_taken = findLIS(index + 1, prev)
            
            # Return the maximum of including or not including the current element
            return max(taken, not_taken)
        
        # Start the recursion with index 0 and a very small previous value
        return findLIS(0, float('-inf'))
```

### baisc Dynamic Programming solution

```Python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
        
        return max(dp)
```

### Optimised Dynamic Programming solution
- `bisect_left` is a function in the `bisect` module that returns the index of the leftmost value greater than or equal to the target value in a sorted array

```Python
def lengthOfLIS(nums):
    from bisect import bisect_left
    tails = []
    for num in nums:
        # Binary search: find the leftmost value greater than or equal to num
        index = bisect_left(tails, num)
        if index == len(tails):
            # If num is larger than any in tails, extend tails
            tails.append(num)
        else:
            # Otherwise, replace the first larger or equal element with num
            tails[index] = num

    return len(tails)
```