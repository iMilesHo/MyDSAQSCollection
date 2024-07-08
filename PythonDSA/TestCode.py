class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
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