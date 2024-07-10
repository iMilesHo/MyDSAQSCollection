class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = int((left + right) / 2)
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                mid = int((left + right) / 2)
            else:
                right = mid - 1
                mid = int((left + right) / 2)
        if nums[mid] < target:
            return mid + 1
        else:
            return mid