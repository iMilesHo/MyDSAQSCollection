class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        start = 1
        end = num
        mid = (start + end) // 2
        while start <= end:
            target = mid**2
            if target == num:
                return True
            elif target < num:
                start = mid + 1
                mid = (start + end) // 2
            else:
                end = mid - 1
                mid = (start + end) // 2
        return False   