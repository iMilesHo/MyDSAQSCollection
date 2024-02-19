#  1071. Greatest Common Divisor of Strings
## fileNmae: 10_1071_Greatest_Common_Divisor_of_Strings.md

## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/greatest-common-divisor-of-strings/description/).

## constraints:
constraints:
- both string length: [1, 1000]
- both strings ara uppercase English
- return "" if there is not x

## idea:
- split a substring from the longer on which the length is from len(shorter one) to 1 or from 1 to len(shorter one)
- judge if this substring can divide both the input strings using String.count(subString) 

### Notes:
- We could just use the substring of the shorter one which is always starting from 0 to explore the GCD of the two strings, since only if every substring including the first one can divide both the input strings, then it is the GCD of the two strings.

## test cases:
- "ABCABC", "ABC"
             ABC

## Python Solution

### My own solution
```Python
# Not the best solution
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        longer_one = ""
        shorter_one = ""
        if len(str1) <= len(str2):
            longer_one = str2
            shorter_one = str1
        else:
            longer_one = str1
            shorter_one = str2
        GCD_ans = ""
        for i in range(len(shorter_one)):
            subString = shorter_one[0:(i+1)]
            if shorter_one.count(subString)*(i+1) == len(shorter_one) and longer_one.count(subString)*(i+1) == len(longer_one):
                GCD_ans = subString
        return GCD_ans
```

### leetcode solution
```Python
# Fastest solution
"""
math.gcd used to find the greatest common divisor
Usage: math.gcd(a, b), where a and b are two length of the strings

"""
class Solution:
    from math import gcd
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        return str1[:gcd(len(str1), len(str2))]
```

