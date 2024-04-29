from typing import List
from traitlets import Int

def mergeSort(arr: List[int]) -> List[int]:
    length_arr = len(arr)
    if length_arr <= 1:
        return arr
    left = mergeSort(arr[:length_arr//2])
    right = mergeSort(arr[length_arr//2:])

    left_i, right_i = 0, 0
    for i in range(len(left)+len(right)):
        if (left_i < len(left) and left[left_i] <= right[left_i]) or right_i >= len(right):
            arr[i] = left[left_i]
            left_i += 1
        elif (right_i < len(right) and left[left_i] > right[left_i]) or left_i >= len(left):
            arr[i] = right[right_i]
            right_i += 1
    return arr


# Test

arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(mergeSort(arr))