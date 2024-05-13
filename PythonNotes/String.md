# String

## Python

### Basics Notions

- Strings are immutable sequences of characters.

```python
s = "Hello World"
s[0] = "h"  # TypeError: 'str' object does not support item assignment

s = "hello world"  # This is allowed
# The original string is not modified, a new string is created. Then the original string is garbage collected.

# Notation,
s = "Hello World"
print(id(s))  # Output: 4548923056
s1 = s
print(id(s1))  # Output: 4548923056
s = "Hello Universe" # a new string is created, and s is pointing to the new string
print(id(s))  # Output: 4545223288
print(id(s1))  # Output: 4548923056
```

- Strings can be enclosed in single quotes ('...') or double quotes ("...").
- Triple quotes ('''...''' or """...""") are used to span the string across multiple lines.
- Escape sequences are used to represent characters that are difficult to type or would be inconvenient to read.

```python
s = "Hello\nWorld"
print(s)  # Output: Hello
          #         World
```

### Basic Operations

- Length: Getting the length of a string using len(string).

```python
s = "Hello World"
print(len(s))  # Output: 11
```

- Concatenation: Combining strings using the + operator.

```python
s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)  # Output: Hello World
```

- Repetition: Repeating strings using the \* operator.

```python
s = "Hello"
s1 = s * 3
print(s1)  # Output: HelloHelloHello
```

- Indexing: Accessing characters by index using string[index].

```python
s = "Hello"
print(s[0])  # Output: H
print(s[1])  # Output: e
```

- Slicing: Getting a substring using string[start:end:step].

```python
s = "Hello World"
print(s[0:5])  # Output: Hello
print(s[6:])  # Output: World
print(s[:5])  # Output: Hello
print(s[::2])  # Output: HloWrd
```

### String Methods

- .find(sub[, start[, end]]): Returns the lowest index where the substring sub is found.

```python
s = "Hello World"
print(s.find("World"))  # Output: 6

```

- .replace(old, new[, count]): Returns a string where all occurrences of 'old' are replaced by 'new'.

```python
s = "Hello World Hello World"
print(s.replace("World", "Universe"))  # Output: Hello Universe Hello Universe
```

- .split(sep=None, maxsplit=-1): Returns a list of the words in the string, using sep as the delimiter.

```python
s = "Hello World"
print(s.split())  # Output: ['Hello', 'World']
print(s.split("o"))  # Output: ['Hell', ' W', 'rld']
```

- .join(iterable): Joins an iterable of strings with the string acting as the separator.

```python
s = " "
print(s.join(["Hello", "World"])) # Output: Hello World
```

- .strip([chars]): Returns a copy of the string with leading and trailing characters removed.

```python
s = "  Hello World  "
print(s.strip())  # Output: Hello World, leading and trailing spaces removed
print(s.strip("  "))  # Output: Hello World, leading and trailing spaces removed
print(s.strip("  H"))  # Output: ello World, leading and trailing spaces and H removed
```

- .lstrip([chars]), .rstrip([chars]): Similar to .strip(), but for leading and trailing characters, respectively.
- .upper(), .lower(): Returns a copy of the string converted to uppercase or lowercase.

```python
s = "Hello World"
print(s.upper())  # Output: HELLO WORLD
print(s.lower())  # Output: hello world
```

- .title(): Returns a title-cased version of the string.

```python
s = "hello world"
print(s.title())  # Output: Hello World
```

- .startswith(prefix[, start[, end]]), .endswith(suffix[, start[, end]]): Returns True if the string starts or ends with the specified prefix/suffix.

```python
s = "Hello World"
print(s.startswith("Hello"))  # Output: True
print(s.endswith("World"))  # Output: True
```

- .isdigit(), .isalpha(), .isalnum(), .isspace(): Return True if all characters in the string are digits, alphabetic, alphanumeric, or whitespace, respectively.

```python
s = "Hello World"
s1 = "123"
s2 = "HelloWorld123"
print(s.isdigit())  # Output: False
print(s.isalpha())  # Output: False
print(s.isalnum())  # Output: False
print(s.isspace())  # Output: False
print(s1.isdigit()) # Output: True
print(s1.isalpha()) # Output: False
print(s1.isalnum()) # Output: True
print(s1.isspace()) # Output: False
print(s2.isdigit()) # Output: False
print(s2.isalpha()) # Output: False
print(s2.isalnum()) # Output: True
print(s2.isspace()) # Output: False
```

### Formatting

- .format(\*args, \*\*kwargs): Formats the string using format specification.

```python
s = "Hello {}"
print(s.format("World"))  # Output: Hello World
print("Hello {0}, {1}".format("World", "Universe"))  # Output: Hello World, Universe
```

- f-strings (formatted string literals): Allows including expressions inside string literals, using {expression}.

```python
name = "World"
print(f"Hello {name}") # Output: Hello World
```

- .center(width[, fillchar]), .ljust(width[, fillchar]), .rjust(width[, fillchar]): Methods for aligning strings within a specified width.

````python
s = "Hello"
print(s.center(10, "-"))  # Output: --Hello---
### Searching and Matching
- .count(sub[, start[, end]]): Returns the number of non-overlapping occurrences of substring sub in the string.
```python
s = "Hello World"
print(s.count("o")) # Output: 2
print(s.count("o", 0, 5)) # Output: 1
````

## String interning

- Python automatically interns certain strings, storing only one copy of the string in memory even if it appears multiple times in a program.
- Strings that look like identifiers are more likely to be interned automatically.
- You can force strings to be interned using the sys.intern() function.
- Whether or not strings are interned can depend on how they are created and what they contain. Some strings are not interned automatically (e.g., strings created at runtime through concatenation).

# Cheat Sheet - Python String

```python
s = "Tom is a name of a dog, and  a dog is called Tom"
s1 = 'Tom is a name of a dog'
# s[0] = "t"  # TypeError: 'str' object does not support item assignment
print(id(s))  # Output: 4548923056
print(id(s1))  # Output: different one

print(s == s1)  # Output: True, s and s1 are equal in value
s1 += ", and  a dog is called Tom"
print(s == s1)

print(len(s))  # Output: 48

s2 = "Bye"
s3 = s2 * 3
print(s3)  # Output: ByeByeBye

print(s[::-1])
print(s[0:3])  # Output: Tom

print(s.find("dog"))  # Output: 18, the first index of the substring "dog" which is the first occurrence of "dog"
print(s.find("dog", 19))  # search for "dog" starting from index 19, Output: 38
print(s.replace("dog", "cat"))  # Output: Tom is a name of a cat, and  a cat is called Tom

print(s.split())  # Output: ['Tom', 'is', 'a', 'name', 'of', 'a', 'dog,', 'and', 'a', 'dog', 'is', 'called', 'Tom']

print(list(s)) # Output: ['T', 'o', 'm', ' ', 'i', 's', ' ', 'a', ' ', 'n', 'a', 'm', 'e', ' ', 'o', 'f', ' ', 'a', ' ', 'd', 'o', 'g', ',', ' ', 'a', 'n', 'd', ' ', ' ', 'a', ' ', 'd', 'o', 'g', ' ', 'i', 's', ' ', 'c', 'a', 'l', 'l', 'e', 'd', ' ', 'T', 'o', 'm']
print(set(s)) # Output: {' ', 'o', 'T', 'm', 'i', 's', 'a', 'n', 'e', 'f', 'd', 'g', 'c', 'l', 'k', 'T'}


print("".join(list(s)))

print(s.strip())  # Output: Tom is a name of a dog, and  a dog is called Tom

print(s.upper())  # Output: TOM IS A NAME OF A DOG, AND  A DOG IS CALLED TOM
print(s.lower())  # Output: tom is a name of a dog, and  a dog is called tom
print(s.title())  # Output: Tom Is A Name Of A Dog, And  A Dog Is Called Tom

s = "Hello {0}, {1}"
print(s.format("World", "Universe"))  # Output: Hello World, Universe
name = "World"
print(f"Hello {name}") # Output: Hello World
```

# Algorithm - String

Techniques for solving string-related problems:

- Two-pointer technique: often used for palindrome problems or substring problems.
- Hashing: useful for counting characters or checking anagrams.
- Dynamic programming: for edit distance, longest common subsequence, or other transformation problems.
- Sliding window: for substrings with specific properties like longest substring without repeating characters.
- Prefix sum: for substring sum problems.
- KMP algorithm: for pattern matching problems.
- Rabin-Karp algorithm: for pattern matching problems.
- Z algorithm: for pattern matching problems.
- Aho-Corasick algorithm: for multiple pattern matching problems
- Manacher's algorithm: for finding the longest palindromic substring.

Python-Specific Techniques:

- Using the `collections` module for counting characters or creating a dictionary with default values.
- List comprehension for string manipulation.
- Using `re` module for regular expressions.
- Using the `str` class methods for string manipulation.

# transform between string, integer, float, list, tuple, set, dictionary

```python
# String to Integer
s = "123"
i = int(s)

# String to Float
s = "3.14"
f = float(s)

# Integer/Float to String
i = 123
f = 3.14
s1 = str(i)
s2 = str(f)

# String/Tuple/Set to List
s = "Hello"
t = (1, 2, 3)
se = {1, 2, 3}
l1 = list(s)
l2 = list(t)
l3 = list(se)

# List/Tuple/Set to String
l = ['H', 'e', 'l', 'l', 'o']
t = (1, 2, 3)
se = {1, 2, 3}
s1 = "".join(l)
s2 = "".join(map(str, t))
s3 = "".join(map(str, se))

# to Tuple are similar to List
l = ['H', 'e', 'l', 'l', 'o']
t = tuple(l)

# to set are similar to List
l = ['H', 'e', 'l', 'l', 'o']
se = set(l)

# List of Pairs/Tuple of Pairs to Dictionary
l = [("a", 1), ("b", 2), ("c", 3)]
t = (("a", 1), ("b", 2), ("c", 3))
d1 = dict(l)
d2 = dict(t)

# Dictionary to List of Pairs/Tuple of Pairs
d = {"a": 1, "b": 2, "c": 3}
l = list(d.items())
t = tuple(d.items())

l1 = [(1, 2), (3, 4), (5, 6), (1,2)]
s1 = set(l1)
print(s1) # Output: {(1, 2), (3, 4), (5, 6)}
```

# Counter and defaultdict

```python
from collections import Counter, defaultdict

# Creating a Counter
c = Counter('abcdeabcdabcaba')  # count elements from a string

print(c.most_common(2))

c.update('aaaaazzz')
print(c)

c.subtract('aaa')
print(c)

print(c.elements())
print(list(c.elements()))

# Creating a defaultdict
from collections import defaultdict

# Using list as the default_factory
dd = defaultdict(list)
print(dd)  # Output: defaultdict(<class 'list'>, {})
words = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
for k, v in words:
    dd[k].append(v)

print(dd)  # defaultdict(<class 'list'>, {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]})

# Using int as the default_factory (for counting)
dd_int = defaultdict(int)
print(dd_int)  # Output: defaultdict(<class 'int'>, {})
for word in 'abracadabra':
    dd_int[word] += 1 # the default value is 0

print(dd_int)  # defaultdict(<class 'int'>, {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
```

## Common Problems

- Check if a string is a palindrome.

```python
def is_palindrome(s):
    return s == s[::-1]
```

- Check if a string is an anagram of another string.

```python
from collections import Counter
def are_anagrams(s1, s2):
    return Counter(s1) == Counter(s2)
```

- Longest Substring Without Repeating Characters

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        if length <= 1:
            return length

        char_index_dict = {}
        max_len = float("-inf")
        start = 0

        for end in range(len(s)):
            # update the start
            if s[end] in char_index_dict and char_index_dict[s[end]] >= start:
                start = char_index_dict[s[end]] + 1
                char_index_dict[s[end]] = end

            # update the dict
            char_index_dict[s[end]] = end
            max_len = max(max_len, end - start +1)

        return max_len
```

- Longest Palindromic Substring

```python
# brute force
class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            for j in range(i,len(s)+1):
                temp = s[i:j]
                if temp == temp[::-1] and len(temp) > len(ans):
                    ans = temp
        return ans

# dynamic programming
def longest_palindromic_substring_dp(s):
    n = len(s)
    if n == 0:
        return ""

    longest = s[0]
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > len(longest):
                        longest = s[i:j+1]

    return longest

# expand around center
def longest_palindromic_substring_expand(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # Odd length palindromes
        tmp = expand_around_center(i, i)
        if len(tmp) > len(longest):
            longest = tmp
        # Even length palindromes
        tmp = expand_around_center(i, i + 1)
        if len(tmp) > len(longest):
            longest = tmp
    return longest
```

- Longest Common Subsequence

```python

```

- Edit Distance

```python

```

- Substring Search

```python

```
