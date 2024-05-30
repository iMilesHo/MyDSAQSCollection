# 78. Subsets

## Solution

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        solution = []
        def dfs(index):
            if index == n:
                result.append(solution[:])
                return
            solution.append(nums[index])
            dfs(index + 1)
            solution.pop()
            dfs(index + 1)
        dfs(0)
        return result
```

## Notes:

- For each element, we have two choices: either include it in the subset or exclude it.
- the initial solution is an empty list.
  - then we first focus on the first element, and we have two choices: include it or exclude it.
  - solution.append(nums[0])
  - dfs(1)
  - solution.pop()
  - dfs(1)
- it's a binary tree, and each layer of the tree represents the current all possible subsets.
- we can use a recursive function to solve this problem.

## Complexity Analysis

- Time complexity: O(2^n\*n)
- Space complexity: O(2^n\*n)
