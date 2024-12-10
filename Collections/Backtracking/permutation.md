# Permutations

## Solution

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]: # nums =  [1, 2, 3]
        res = []
        used = set()
        prmt = []

        def dfs():
            if len(prmt) == len(nums): # prmt = [1, ]
                res.append(prmt[:]) # [[1, 2, 3], ]
                return

            for i in nums: # 1
                if i not in used: # used = {1, 3, 2 }
                    used.add(i)
                    prmt.append(i)
                    dfs()
                    used.remove(i)
                    prmt.pop()
        dfs()
        return res
```
