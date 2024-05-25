# name: 54 - Remove 0 and 1 from string

Given a string str,
1.if there is a '0' in the String , remove the '0' and the '1' if there is a 1 next to zero on either side
2.You can do the above operationg multiple times
3.There can be special characters , in that case , the deletion cannot be performed.
Print the length of the final string after deletion
Input: str = “11010”
The resultant string will be “1” . So output is 1
Input: str = “111000”
Resultant string, str = “” . So output is 0
Input: str = “111&000”
Resultant string, str = “111&000” . So output is 7

```python
def HackerRank(s):
  if not s or s == "":
    return 0
  stack = []
  for c in s:
    if len(stack) > 0 and ((c == '0' and stack[-1] == '1') or (c == '1' and stack[-1] == '0')):
      stack.pop()
    else:
      stack.append(c)
  return len(stack)


# test cases
print(HackerRank("1100")) # 0
print(HackerRank("1111")) # 4
print(HackerRank("01010")) # 1
print(HackerRank("010101")) # 0
print(HackerRank("111&000")) # 0
```
