# 268. Missing Number

## filename: 18_268_missing_number.md

## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/missing-number/description/).


## Python Solution

### Method 1: Using set
```Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums_set = set(nums)
        for number in range(n+1):
            if number not in nums_set:
                return number
```

### Method 2: Using XOR
```Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing
```

### Method 3: Using Gauss' Formula
```Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum
```

### Method 4: Using Sorting
```Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] != 1:
                return nums[i-1] + 1
        return len(nums)
```

### Method 5: Using Binary Search
```Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > mid:
                right = mid
            else:
                left = mid + 1
        return left
```

### Method 6: Using Hash Map
```Python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_map = {num: 1 for num in nums}
        for number in range(len(nums)+1):
            if number not in nums_map:
                return number
```