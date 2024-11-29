# 347. Top K Frequent Elements

## idea:
- map:
 - key -> nums_value
 - value -> frequency
- sort map according to 

## Python Solution
### My Method
```Python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        frequency_dict = {}
        ans = []
        for i in nums:
            if i not in frequency_dict.keys():
                frequency_dict[i] = 1
            else:
                frequency_dict[i] += 1
        frequency_dict_sorted_list = sorted(frequency_dict.items(), key = lambda i: i[1], reverse=True)
        for i, (key, value) in enumerate(frequency_dict_sorted_list):
            if i >= k:
                break
            ans.append(key)
        return ans
```

### Method 1: Using Counter
```Python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in Counter(nums).most_common(k)]
```

### Method 2: Using Heap
```Python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
```

### Method 3: Using Bucket Sort
```Python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in count.items():
            bucket[value].append(key)
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k]
```
#### Note
- `flat_list[::-1]` is to reverse the list
```Python
l = [1, 2, 3, 4, 5]
print(l[::-1]) # [5, 4, 3, 2, 1]
print(l[::-2]) # [5, 3, 1]

print(l[::1]) # [1, 2, 3, 4, 5]
print(l[::2]) # [1, 3, 5]
```
