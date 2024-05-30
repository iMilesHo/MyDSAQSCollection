# 1822. Sign of the Product of an Array

## Problem Statement
Check the problem statement [here](https://leetcode.com/problems/sign-of-the-product-of-an-array/description/).

## Solution


###  Constraints:
input is an array
nums.length-[1,1000]
nums[i]-[-100,100]
return 0, 1 or -1

### idea1:
ans = 1
if nums[i] == 0: return 0
elif nums[i] < 0:
	ans *= -1;

Time complexity: O(n)
Space complexity: O(1)

### Test cases:
[1]
[0]
[1,2]
[1,2,0]
[1,0,2]

### Python

#### My own solution

```Python
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        ans = 1
        for i in nums:
			if i == 0: 
				return 0
			elif i < 0:
				ans *= -1;
		return ans
```

#### LeetCode's solution

```Python
# Approach 1
import math
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        m = math.prod(nums)
        if m == 0: 
            return 0
        if m > 0:
            return 1
        return -1
# Time complexity: O(n)
# Space complexity: O(1)
"""
math.prod(nums) returns the product of all elements in the list nums.

"""
```

```Python
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        if product ==0:
            return 0
        if product > 0:
            return 1
        else:
            return -1

# Time complexity: O(n)
# Space complexity: O(1)
```

```Python
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        mul = 1
        for num in nums:
            mul *= num
        return mul // abs(mul) if mul != 0 else 0
# Time complexity: O(n)
# Space complexity: O(1)
```

```Python
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        c=0
        if(0 in nums):
            return 0
        for i in nums:
            if(i<0):
                c=c+1
        if(c%2==0):
            return 1
        else:
            return -1
        
# Time complexity: O(n)
# Space complexity: O(1)
```


### Java

#### My own solution

```Java
class Solution {
    public int arraySign(int[] nums) {
        int negativeNumber = 0;
        for(int num: nums){
            if(num==0){
                return 0;
            } else if (num<0) {
                negativeNumber += 1;
            }
        }

        if(negativeNumber%2 == 0){
            return 1;
        } else {
            return -1;
        }
    }
}
// Time complexity: O(n)
// Space complexity: O(1)
```

