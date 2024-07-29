class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            pre = i - 1
            cur = i
            while pre >= 0 and nums[cur] < nums[pre]:
                nums[pre], nums[cur] = nums[cur], nums[pre]
                cur = pre
                pre = cur - 1
        return nums