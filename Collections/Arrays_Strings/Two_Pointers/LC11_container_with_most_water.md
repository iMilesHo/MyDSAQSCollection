#  11. Container With Most Water

## solution 1: brute force
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_v = float("-inf")
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                v = (j - i)*min(height[i], height[j])
                if v > max_v:
                    max_v = v
        return max_v
```

## solution 2: two pointers
```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            maxArea = max(maxArea, currentArea)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea
```
