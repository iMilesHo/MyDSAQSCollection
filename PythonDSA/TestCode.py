from typing import List
from traitlets import Int

def binarySearch(arr: List[int], k: int) -> int:
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 1
print(binarySearch(arr, k))