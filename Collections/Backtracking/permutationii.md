# Permutations II

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

## Solution

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        from collections import Counter
        n = len(nums)
        nums_set = set(nums)
        used = Counter(nums)
        prmt = []
        res = []

        def dfs():
            if len(prmt) == n:
                res.append(prmt[:])
                return

            for i in nums_set:
                if used[i] > 0:
                    used[i] -= 1
                    prmt.append(i)
                    dfs()
                    prmt.pop()
                    used[i] += 1
        dfs()

        return res
```
