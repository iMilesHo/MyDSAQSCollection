#  977. Squares of a Sorted Array

## Solution 1
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] >= 0:
                break
            nums[i] = abs(nums[i])
        nums.sort()
        return [i*i for i in nums]
```

## Solution 2
```python
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start = 0
        end = len(nums) - 1
        ans = [0] * len(nums)
        index = end
        while start <= end:
            if abs(nums[start]) > abs(nums[end]):
                ans[index] = nums[start]*nums[start]
                start += 1
            else:
                ans[index] = nums[end] * nums[end]
                end -= 1
            index -= 1
        return ans
```