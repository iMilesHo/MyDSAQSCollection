# 136. Single Number

## constraints

- length: [1, 3 * 10^4]
- value: [-3 * 10^4, 3 * 10^4]

## ideas
- Use a set to store the unique elements
- Iterate through the list and remove the element from the set if it is already present
- The remaining element in the set is the single number



## Python Solution

### My Solution
```Python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(0,len(nums)-1,2):
            if nums[i] != nums[i+1]:
                return nums[i]
        return nums[-1]     
```

### Method 1: Using set
```Python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
```

### Method 2: Using XOR
```Python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
```

### Method 3: Using Math
```Python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)
```

### Method 4: Using Sorting
```Python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(0, len(nums), 2):
            if i == len(nums) - 1:
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]
```