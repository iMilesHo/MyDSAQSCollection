#  441. Arranging Coins

## Solution 1
```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum = 0
        index = 1
        while sum < n:
            sum += index
            index += 1
        if sum == n:
            return index - 1
        else:
            return index - 2
```

## Solution 2
```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + sqrt(1 - 4 * -2 * n))/2)
```

## Solution 3
```python
class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        left, right = 1, n
        
        while left <= right:
            mid = (left + right) // 2
            total = mid * (mid + 1) // 2
            if total == n:
                return mid
            elif total < n:
                left = mid + 1
            elif total > n:
                right = mid - 1
        return right
```
