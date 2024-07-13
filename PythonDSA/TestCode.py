class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 3:
            if target in nums:
                return nums.index(target)
            else:
                return -1

        left, right = 0, len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] > nums[-1]:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        minimum_index = left

        # 0, minimum_index - 1
        left, right = 0, minimum_index - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        # minimum_index, len(nums) - 1
        left, right = minimum_index, len(nums) - 1
        mid = (left + right) // 2
        while left <= right:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
                mid = (left + right) // 2
            else:
                right = mid - 1
                mid = (left + right) // 2
        return -1