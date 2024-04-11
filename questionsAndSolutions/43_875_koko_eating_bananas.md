#  875. Koko Eating Bananas

## solution 1: binary search
```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k: int):
            temp_h = h
            for i in piles:
                if temp_h <= 0:
                    return False
                if i <= k:
                    temp_h -= 1
                else:
                    temp = math.ceil(i/k)
                    temp_h -= temp
            if temp_h < 0:
                return False
            else:
                return True

        left, right = 1, max(piles)
        mid = (left + right) // 2

        while left <= right:
            if not check(mid):
                left = mid + 1 # finally left will be the smallest k
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        return left
```