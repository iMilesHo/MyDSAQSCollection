# 242. Valid Anagram

## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/valid-anagram/description/).

## Solution

- Constraint:
    - input two Strings, both length - [1, 5*10^4]
    - both are lowercase

- idea:
if len(s) != len(t): return false
else:
    dict_s = dict()
    for i in s:
        if dict.key does not contain i:
            dict_s[i] = 1;
        else:
            dict_s[i] += 1;
    // do the same on t

    for i 
- time complexity: O(n+m)
- space complexity:O(n+m)

### Python

#### My own solution

```Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s = {}
        dict_t = {}

        for i in s:
            if dict_s.get(i) is None:
                dict_s[i] = 1
            else:
                dict_s[i] += 1

        for i in t:
            if dict_t.get(i) is None:
                dict_t[i] = 1
            else:
                dict_t[i] += 1

        for key in dict_s:
            if (dict_t.get(key) is None) or (dict_t[key] != dict_s[key]):
                return False
        return True
```

#### LeetCode's solution

```Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # simplest one - with counter
        from collections import Counter
        return Counter(s) == Counter(t)
# Time complexity: O(n+m)
# Space complexity: O(n+m)
```

```Python        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = Counter(list(s))
        count_t = Counter(list(t))
        if len(count_s)!=len(count_t):
            return False
        for key,count in count_s.items():
            if count_s[key]!=count_t[key]:
                return False
            
        return True
# Time complexity: O(n+m)
# Space complexity: O(n+m)
```

```Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)
# Time complexity: O(nlogn)
# Space complexity: O(1)
```

```Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def counter(x):
            count = {}
            for char in x:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
            return count
        
        return counter(s) == counter(t)
# Time complexity: O(n+m)
# Space complexity: O(n+m)
```

```Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t):
            return False
        else:
            count = defaultdict(int)

            for l in s:
                count[l] += 1
            for l in t:
                count[l] -= 1

            for val in count:
                if not count[val] == 0:
                    return False
            return True
# Time complexity: O(n+m)
# Space complexity: O(n+m)
```

```Python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # Initialize a dictionary to store character counts
        char_count = {}
        
        # Update character counts for string s
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # Update character counts for string t
        for char in t:
            char_count[char] = char_count.get(char, 0) - 1
            # If the count becomes negative, t has more of this character than s
            if char_count[char] < 0:
                return False
        
        # Check if all character counts are zero
        return all(count == 0 for count in char_count.values())
# Time complexity: O(n+m)
# Space complexity: O(n+m)
```



## Note

- How to check if a Key exists in a dictionary?
    - ref: [link](https://pieriantraining.com/how-to-check-if-a-key-exists-in-a-python-dictionary/)
    - using 'in' keyword
        - if 'apple' in my_dict:
    - get() method
        - if person.get('name'):
        - if person.get('name') is None:
        - if person.get('name') is not None:
    - Using try/except
        - try:
            - print(person['name'])
        - except KeyError:
            - print('Key not found')
    - using keys() method
        - if 'name' in person.keys():

- How `==` operator works for dictionary in Python?
    - Two dictionaries are equal if they have the same keys and the same values.

- How to use Counter in Python?
    - ref: [link](https://miguendes.me/the-best-way-to-compare-two-dictionaries-in-python)
    - 

- How to use defaultdict in Python?
