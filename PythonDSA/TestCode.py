from collections import Counter
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, value in count.items():
            bucket[value].append(key)
        flat_list = [item for sublist in bucket for item in sublist]
        return flat_list[::-1][:k] # [::-1] reverse the list
    
# test code
s = Solution()
print(s.topKFrequent([1,1,1,2,2,3], 2))