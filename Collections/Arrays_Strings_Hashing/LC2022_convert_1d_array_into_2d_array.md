# 2022. Convert 1D Array Into 2D Array

## you can find the problem [here](https://leetcode.com/problems/convert-1d-array-into-2d-array/description/)

## constraints:
- length of the original array: [1,5*10^4]
- value of the elements in the array: [1,10^5]
- m,n: [1,10^4]

## ideas:
- firstly, if m*n != len(original): return []
- then, use the slice operation

## Python Solution

### My Solution
```Python
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        ans = []
        for i in range(m):
            ans.append(original[i*n:i*n+n])
        return ans
```

### Method 1: Using List Comprehension
```Python
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        return [original[i*n:i*n+n] for i in range(m)]
```

### Method 2: yield
The yield statement suspends a function’s execution and sends a value back to the caller, but retains enough state to enable the function to resume where it left off. When the function resumes, it continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list.

```Python
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        for i in range(0, len(original), n):
            yield original[i:i+n]
```
