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