class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        mid = int((left + right) / 2)
        while left <= right:
            if guess(mid) == 0:
                return mid
            elif guess(mid) == 1:
                left = mid + 1
                mid = int((left + right) / 2)
            else:
                right = mid - 1
                mid = int((left + right) / 2)
        return None