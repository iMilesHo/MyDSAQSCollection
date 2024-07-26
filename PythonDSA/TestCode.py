class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums)
            
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while left <= right:
            if nums[mid] > nums[-1]:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        return nums[left]   