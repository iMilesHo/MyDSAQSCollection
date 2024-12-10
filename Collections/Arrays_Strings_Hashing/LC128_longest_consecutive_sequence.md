# 128. Longest Consecutive Sequence

## Python Solution

### My Solution

```python
"""
constraints:
- length of the array: [0, 10^5]
- value: [-10^9, 10^9]

idea:
- bucket sort
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        value_dict = {}
        for i in nums:
            value_dict[i] = False
        longest_ans = 0
        for i in nums:
            if value_dict[i]:
                continue
            
            temp_length = 1
            j = i + 1
            while value_dict.get(j) is not None:
                temp_length += 1
                value_dict[j] = True
                j += 1
                
            
            k = i - 1
            while value_dict.get(k) is not None:
                temp_length += 1
                value_dict[k] = True
                k -= 1

            value_dict[i] = True
            if temp_length > longest_ans:
                longest_ans = temp_length
        return longest_ans


        
```

### LeetCode Solution

```python
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
            res = 0
            for num in nums:
                if num - 1 not in nums:
                    nextNum = num + 1
                    while nextNum in nums:
                        nextNum += 1
                    res = max(res, nextNum - num)
            return res
```