class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif mid % 2 == 0:
                if nums[mid] == nums[mid+1]:
                    left = mid + 1
                    mid = (left + right) // 2
                else:
                    right = mid - 1
                    mid = (left + right) // 2
            else:
                if nums[mid] != nums[mid+1]:
                    left = mid + 1
                    mid = (left + right) // 2
                else:
                    right = mid - 1
                    mid = (left + right) // 2
        
        return nums[mid] 