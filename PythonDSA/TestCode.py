class Solution:
    def binarySearch(self, nums: List[int], target) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1


    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = target // 2
        if nums.count(temp) >= 2:
            index1 = nums.index(temp)
            index2 = nums.index(temp, index1+1)
            return [index1, index2]

        nums_copy = nums.copy()
        nums.sort()
        for i in range(len(nums)):
            temp = target - nums[i]
            temp_index = self.binarySearch(nums,temp)
            if temp_index == -1:
                continue
            if temp_index != i:
                return [nums_copy.index(nums[i]), nums_copy.index(nums[temp_index])]