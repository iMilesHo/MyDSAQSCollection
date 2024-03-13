from typing import List

"""
constraints:
- length of the array: [0, 10^5]
- value: [-10^9, 10^9]

idea:
- bucket sort
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        value_dict = {}
        for i in nums:
            value_dict[i] = False
        longest_ans = 0
        for i in nums:
            if value_dict[i]:
                continue
            
            temp_length = 1
            j = i + 1
            while value_dict.get(j) is not None:
                temp_length += 1
                value_dict[j] = True
                j += 1
                
            
            k = i - 1
            while value_dict.get(k) is not None:
                temp_length += 1
                value_dict[k] = True
                k -= 1

            value_dict[i] = True
            if temp_length > longest_ans:
                longest_ans = temp_length
        return longest_ans


sol = Solution() 
print(sol.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6])) # 4