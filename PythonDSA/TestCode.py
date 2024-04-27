from typing import List
from traitlets import Int

def isPalindromeAnagram(word: str) -> bool:
    left, right = 0, len(word) - 1
    word = word.lower()

    while left < right:
        if word[left].isalnum() and word[right].isalnum():
            if word[left] != word[right]:
                return False
            else:
                left += 1
                right -= 1
        else:
            if not word[left].isalnum():
                left += 1
            if not word[right].isalnum():
                right -= 1

    return True

s = "A man, a plan, a canal: Panama"
print(isPalindromeAnagram(s))