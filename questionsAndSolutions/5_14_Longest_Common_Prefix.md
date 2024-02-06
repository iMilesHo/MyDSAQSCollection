# 14. Longest Common Prefix

## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/longest-common-prefix/description/).

## Solution

### Python

#### My own solution

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        temp = strs[0]
        for i in range(1, len(strs)):
            temp = self.longestCommonPrefixBetween(temp, strs[i])
        return temp
    
    def longestCommonPrefixBetween(self, str1: str, str2: str) -> str:
        ans = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                ans += str1[i]
            else:
                return ans
        return ans
```

#### LeetCode's solution

```python
# Approach 1
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        def compare(A, B):
            t = ''
            # zip() function returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.
            for a, b in zip(A, B):
                if a == b:
                    t += a
                else:
                    return t
            return t
        for word in strs[1:]:
            prefix = compare(prefix, word) 
        return prefix
# Time complexity: O(S), where S is the sum of all characters in all strings.
# Space complexity: O(1)
```

```python
# Approach 2: Vertical scanning
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or strs[0][i] != word[i]:
                    return res
            res += word[i]
        return res
# Time complexity: O(S), where S is the sum of all characters in all strings.
# Space complexity: O(1)
```

```python
# Approach 3
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for s, *p in zip(*strs):
            if all(s == c for c in p):
                prefix += s
            else:
                break
        
        return prefix
# Time complexity: O(S), where S is the sum of all characters in all strings.
# Space complexity: O(1)

'''
1. The zip Function
The zip(*iterables) function takes iterables (like lists, strings, etc.), aggregates them into a tuple, and returns an iterator of tuples. Each tuple contains the elements from the iterables that are at the same position. If the iterables are of different lengths, zip stops creating tuples when the shortest iterable is exhausted.

2. The * Operator for Unpacking
The * operator is used to unpack iterables in Python. When used with zip, like zip(*strs), it unpacks the list strs so that each string in strs is passed as a separate argument to zip. This effectively transposes the list of strings, so you get an iterator of tuples, where each tuple contains the characters from each string at a particular index.
'''
```


### Java

#### My own solution

```java
class Solution {
    public String longestCommonPrefixBetween(String str1, String str2) {
        String longestCommonPrefrix = "";
        int minLength = Math.min(str1.length(), str2.length());
        for (int i=0; i<minLength; i++) {
            if(str1.charAt(i)==str2.charAt(i)){
                longestCommonPrefrix += str1.charAt(i);
            } else {
                return longestCommonPrefrix;
            }
        }
        return longestCommonPrefrix;
        
    }
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];
        for(int i=1; i<strs.length; i++){
            prefix = longestCommonPrefixBetween(prefix, strs[i]);
        }
        return prefix;
    }
}
// Time complexity: O(n*m), where n is the number of strings and m is the length of the longest string.
// Space complexity: O(1)
```

#### LeetCode's solution

```java
// Approach 1
class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        String s1 = strs[0];
        String s2 = strs[strs.length-1];
        int i=0;
        while(i<s1.length() && i<s2.length()){
            if(s1.charAt(i)==s2.charAt(i)){
                i++;
                }else{
                    break;
            }
        }
        return s1.substring(0,i);
    }
}
// Time complexity:
// the sort function takes O(nlogn) time, where n is the number of strings.
// The comparison takes O(m) time, where m is the length of the common prefix.
// So, the overall time complexity is O(nlogn + m).
// Space complexity: O(m), where m is the length of the common prefix.

//Breakdown:
// 1. Sort the input strings:
//    The sorting comparison is according to the lexicographical order, so the common prefix of the first and last strings is the longest common prefix.
// 2. Compare the first and last strings
```

```java
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if(strs==null || strs.length==0){
            return "";
        }
        String prefix = strs[0];
        for(int i=1;i<strs.length;i++){
            while(strs[i].indexOf(prefix)!=0){
                prefix =prefix.substring(0,prefix.length()-1);
            }
        }

        return prefix;  
    }
}
// Time complexity: 
// O(n*m*m), where n is the number of strings and m is the length of the longest string.
// Space complexity: O(1)

//Breakdown:
/*
1. The String Method
public int indexOf(int ch)
public int indexOf(String str, int fromIndex)

String indexOf() function returns the index within the string of the first occurrence of the specified substring.
If no such index is found, -1 is returned.
But in the below cases:
Case 1:
String s1 = "Hello";
String s1 = "";
s1.indexOf(""); // returns 0
s1.indexOf("H"); // returns 0
s1.indexOf("l"); // returns 2

Case 2:
String s1 = "";
String s2 = "Hello";
s1.indexOf(""); // returns -1

Case 3:
String s1 = "";
String s2 = "";
s1.indexOf(""); // returns 0

2. The String substring() Method
public String substring(int beginIndex)
public String substring(int beginIndex,int endIndex)
*/
```



