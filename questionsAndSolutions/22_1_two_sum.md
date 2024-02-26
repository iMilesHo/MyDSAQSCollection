# 1. Two Sum

## constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9

## ideas:
- to achieve O(nlogn) time complexity, we can sort the array and use two pointers to find the target
- achieve a binary search time complexity of O(nlogn)

## Python Solution

### My Method
```Python
class Solution:
    def binarySearch(self, nums: List[int], target) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = target // 2
        if nums.count(temp) >= 2:
            index1 = nums.index(temp)
            index2 = nums.index(temp, index1+1)
            return [index1, index2]

        nums_copy = nums.copy()
        nums.sort()
        for i in range(len(nums)):
            temp = target - nums[i]
            temp_index = self.binarySearch(nums,temp)
            if temp_index == -1:
                continue
            if temp_index != i:
                return [nums_copy.index(nums[i]), nums_copy.index(nums[temp_index])]
```

### Method 1: Using Two Pointers
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(num, i) for i, num in enumerate(nums)]
        nums.sort() # sort according to the first element of the tuple
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left][0] + nums[right][0] == target:
                return [nums[left][1], nums[right][1]]
            elif nums[left][0] + nums[right][0] < target:
                left += 1
            else:
                right -= 1
        return []
```

### Method 2: Using Hash Map
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if target - num in hash_map:
                return [hash_map[target - num], i]
            hash_map[num] = i
        return []
```

### Method 3: Using Brute Force
```Python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```