import sys
from typing import List

def lengthOfLIS_naive(nums):
    # Function to find the length of LIS ending with the last element included
    def findLIS(index, prev):
        # Base case: If we've processed all elements
        if index == len(nums):
            return 0
        
        # Case 1: Exclude the current element and move to the next element
        taken = 0
        if nums[index] > prev:
            # Case 2: Include the current element if it is greater than the previous element in the LIS
            taken = 1 + findLIS(index + 1, nums[index])
        
        not_taken = findLIS(index + 1, prev)
        
        # Return the maximum of including or not including the current element
        return max(taken, not_taken)
    
    # Start the recursion with index 0 and a very small previous value
    return findLIS(0, float('-inf'))

# Example usage
nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS_naive(nums))
