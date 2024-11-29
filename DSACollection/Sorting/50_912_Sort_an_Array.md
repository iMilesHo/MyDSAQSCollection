# 912. Sort an Array

## solution 1: selection sort

```python
# selection sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            cur_min_idx = i
            for j in range(i+1, len(nums)):
                if nums[j] < nums[cur_min_idx]:
                    cur_min_idx = j
            nums[i], nums[cur_min_idx] = nums[cur_min_idx], nums[i]
        return nums
```

## solution 2: insertion sort

```python
# insertion sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            pre = i - 1
            cur = i
            while pre >= 0 and nums[cur] < nums[pre]:
                nums[pre], nums[cur] = nums[cur], nums[pre]
                cur = pre
                pre = cur - 1
        return nums
```

## solution 3: bubble sort

```python
# bubble sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        length_nums = len(nums)
        for i in range(length_nums):
            for j in range(length_nums - i - 1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums
```
