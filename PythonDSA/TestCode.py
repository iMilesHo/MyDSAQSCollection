  from collections import defaultdict

  # Initialize the character count map
  char_count = defaultdict(int)
  required_chars = len(arr)
  left, right = 0, 0
  min_length = float('inf')
  min_substr = ""
  unique_chars = 0


  # Populate the character count map with the characters in arr
  for char in arr:
    char_count[char] = 0

  while right < len(str):

    # Expand the window by including the character at right index
    if str[right] in char_count:
      if char_count[str[right]] == 0:
        unique_chars += 1
      char_count[str[right]] += 1



    while unique_chars == required_chars:
      if right - left + 1 < min_length:
        min_length = right - left + 1
        min_substr = str[left:right+1]
        # update the min_subst
      if str[left] in char_count:
        char_count[str[left]] -= 1
        if char_count[str[left]] == 0:
          unique_chars -= 1
      left += 1

    right += 1
    # check if the new substing is minimum

  return min_substr


# Example usage:
arr = ['x', 'y', 'z']
str = "xyyzyzyx"
print(get_shortest_unique_substring(arr, str))  # Output: "zyx"