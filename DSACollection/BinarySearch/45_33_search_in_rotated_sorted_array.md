#  33. Search in Rotated Sorted Array

## solution 1: my solution
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 3:
            if target in nums:
                return nums.index(target)
            else:
                return -1

        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] > nums[-1]:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        minimum_index = left

        # 0, minimum_index - 1
        left, right = 0, minimum_index - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        # minimum_index, len(nums) - 1
        left, right = minimum_index, len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        return -1
```

## optimization
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Binary search
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            
            # determine which side to check
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target <= nums[right] and target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1
```