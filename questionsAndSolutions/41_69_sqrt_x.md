#  69. Sqrt(x)


Python Notes:
```python
# round half to even or banker's rounding
round(0.5) # 0, since 0 is even while 1 is odd
round(1.5) # 2, since 2 is even while 1 is odd

# round half to up, math.ceil
math.ceil(0.5) # 1
math.ceil(1.5) # 2
```

## Solution 1
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        if x == 0:
            return 0
        start = 1
        end = x
        mid = (start + end) // 2
        while start < end:
            target = mid*mid
            if target == x:
                return mid
            elif target < x:
                start = mid + 1
                mid = (start + end) // 2
            else:
                end = mid - 1
                mid = (start + end) // 2
        target = mid*mid
        
        if target == x:
            return mid
        elif target > x:
            return mid - 1
        else:
            return mid
```
                
        


## Solution 2
```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0 or x == 1):
            return x
        l = 1
        r = x
        while l <= r:
            mid = l+(r-l)//2
            if mid*mid == x:
                return mid
            if mid*mid > x:
                r=mid-1
            else:
                l = mid+1
        return r
```