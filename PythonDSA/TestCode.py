from typing import List

class Solution:
    def is_the_same_anagrams(self, ans, current):
        list_current = list(current)
        list_current.sort()
        is_grouped = False
        for i in ans:
            if len(i[0]) != len(list_current):
                continue
            temp = list(i[0])
            temp.sort()
            is_the_same_anagrams = True
            for cur_i, temp_i in zip(list_current, temp):
                if cur_i != temp_i:
                    is_the_same_anagrams = False
                    break
            if is_the_same_anagrams:
                i.append(current)
                is_grouped = True
                break
        if not is_grouped:
            ans.append([current])
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        for i in strs:
            self.is_the_same_anagrams(ans, i)
        return ans

# test code
            
sol = Solution()
print(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))