# 238. Product of Array Except Self

## Python Solution


### My Solution

```python
"""
contraints:
- ranges as shown on the left side
- all of them are lowercase English letters
- ?: are there any duplicated letters in the original word or phase?

ideas:
- how do I decide two items are the anagrams
    - method 1: set(list(strs[i])) compared with set(list(strs[i+1])), if the equal to each other then I need to check the number of each letter occured in the items, then I can decide if they are the same anagrams.
    - method 2: list(str[i]).sort(), then I check if there are the same step-by-step.
- For ...
"""
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
```

### Official Solution

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check_dict = {}
        for i in strs:
            temp = ''.join(sorted(list(i)))
            if temp in check_dict:
                check_dict[temp].append(i)
            else:
                check_dict[temp] = [i]
        return check_dict.values()
```

### Notes:
- We can store the sorted string as the key of the dictionary, and the value is the list of the original strings.