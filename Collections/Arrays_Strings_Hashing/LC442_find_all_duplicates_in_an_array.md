# 442. Find All Duplicates in an Array

## contraints:
- length n : [1, 10^5]
- elements: [1, n]

## ideas:
- use set
[4,3,2,7,8,2,3,1]

set1: 4,3,2,7,8, 1
set2: 2, 3,

## Python Solution

### My Method
```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        set1 = set()
        ans = []
        for i in nums:
            if i not in set1:
                set1.add(i)
            else:
                ans.append(i)
        return ans
```

### Method 1: Using Counter
```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        from collections import Counter
        return [i for i, j in Counter(nums).items() if j > 1]
```

### Method 2: Using Set
```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        set1 = set()
        ans = []
        for i in nums:
            if i in set1:
                ans.append(i)
            else:
                set1.add(i)
        return ans
```

### Method 3: Using Negative Indexing
#### Idea:
- the elements are in the range of 1 to n
- so we can use the elements as index, and mark the element at that index as negative
```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            if nums[abs(i)-1] < 0:
                ans.append(abs(i))
            else:
                nums[abs(i)-1] *= -1
        return ans
```

### Method 4: Using Sorting
```python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                ans.append(nums[i])
        return ans
```

