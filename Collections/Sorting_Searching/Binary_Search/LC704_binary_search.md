# 704. Binary Search

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = int((left + right) / 2)
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # target is in the right side of index mid
                left = mid + 1
                mid = int((left + right) / 2)
            else:
                right = mid - 1
                mid = int((left + right) / 2)
            
        return -1        
```