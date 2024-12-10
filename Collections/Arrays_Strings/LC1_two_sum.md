#  1. Two Sum
file name: 35_1_two_sum.md

## Solution 1: Two-pass Hash Table
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_index_dict = {}
        for i in range(len(nums)):
            if not nums_index_dict.get(nums[i]):
                nums_index_dict[nums[i]] = [i]
            else:
                nums_index_dict[nums[i]].append(i)

        for i in nums_index_dict:
            remain_value = target - i
            remain_value_indexs = nums_index_dict.get(remain_value)
            if remain_value == i and remain_value_indexs and len(remain_value_indexs) > 1:
                return remain_value_indexs[:2]
            elif remain_value != i and remain_value_indexs:
                return [nums_index_dict[i][0], remain_value_indexs[0]]
        return None  
```

## Solution 2: One-pass Hash Table
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range(n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []  # No solution found
```
