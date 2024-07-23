class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def isExist(ans, new):
            set_new = set(new)
            for i in ans:
                set1 = set(i)
                if set_new == set1:
                    return True
            return False
                
        ans = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        new = [nums[i],nums[j],nums[k]]
                        if not isExist(ans, new):
                            ans.append(new)
        return ans