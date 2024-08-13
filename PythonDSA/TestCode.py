class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        far_left = 0
        far_right = len(s) - 1
        while far_left < far_right:
            if s[far_left] in vowels and s[far_right] in vowels:
                temp = s[far_right]
                s[far_right] = s[far_left]
                s[far_left] = temp
                far_left += 1
                far_right -= 1
            if s[far_left] not in vowels:
                far_left += 1
            if s[far_right] not in vowels:
                far_right -= 1
        return "".join(s)