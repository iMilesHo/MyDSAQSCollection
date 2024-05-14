from typing import List, Optional
from traitlets import Int
from collections import Counter, defaultdict, deque

def two_sum(nums, target):
    complementarys = {}
    for i in range(len(nums)):
        complementary = target - nums[i]
        if complementary not in complementarys:
            complementarys[nums[i]] = i
        else:
            return [complementarys[complementary],i]
    return []

# test
nums = [2,7,11,15]
target = 9
print(two_sum(nums,target))