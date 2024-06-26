class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1
            else:
                res = max(count, res)
                count = 0
        res = max(count, res)
        return res