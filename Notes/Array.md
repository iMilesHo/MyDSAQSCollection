# Array
## Summary
- Array uses a contiguous block of memory to store elements
- Array coonsists of equal-size elements indexed by contiguous integrs
- Array has constant-time access to elements
- Array has constant-time to remove or add elements at the end of the array
- Array has linear-time to remove or add elements at an arbitary location
- 2D Multi-dimensional arrays can be stored through row-major or column-major order
    - (1,1)|(1,2)|(1,3)|(2,1)|(2,2)|(2,3)|(3,1)|(3,2)|(3,3)
    - (1,1)|(2,1)|(3,1)|(1,2)|(2,2)|(3,2)|(1,3)|(2,3)|(3,3)


## Practice

### 1. Print a pascal triangle
```Java
// Java
public class PascalTriangle {
    public static void main(String[] args) {
        int n = 5;
        int[][] pascal = new int[n][];
        for (int i = 0; i < n; i++) {
            pascal[i] = new int[i + 1]; // since java array is 0-based
            pascal[i][0] = 1;
            for(int j=1; j<i; j++) {
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j];
            }
            pascal[i][i] = 1;
        }
    }
}
```

```Python
# Python
def pascal_triangle(n):
    pascal = [[1] * (i+1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
    return pascal
```

# Dynamic Array

## Summary
- Unlike static arrays, dynamic arrays can grow in size
- Appending a new element to a dynamic array is often constant time, but can take O(n) time in the worst case.
- Some space is wasted in dynamic arrays to avoid frequent resizing

## Dynamic Array Definition
Abstract data type with the following operations(at a minimum):
- Get(i): return the element at index i
    - if i is out of bound, return an error message
- Set(i, val): set the element at index i to val
    - if i is out of bound, return an error message
- PushBack(val): append val to the end
    - if the array is full, double the size of the array, and copy the elements to the new array, free the old array, and append val to the end of the new array, update the capacity of the array by doubling the size of the array, and increase the size of the array by 1
- Remove(i): remove the element at index i
- Size(): return the number of elements in the array

## Dynamic Array Implementation
- arr: dynamically-allocated array
- capacity: the maximum number of elements the array can hold
- size: number of elements in the array

## Dynamic Array in C++, Java, and Python
- C++: std::vector
- Java: ArrayList
- Python: list


```C++
// C++
#include <vector>
std::vector<int> v; // create an empty dynamic array
v.push_back(1); // append 1 to the end of the array
v.push_back(2); // append 2 to the end of the array
v.pop_back(); // remove the last element from the array
```

```Java
// Java
import java.util.ArrayList;
ArrayList<Integer> list = new ArrayList<>(); // create an empty dynamic array, the generic type is Integer(int is not allowed)
list.add(1); // append 1 to the end of the array
list.add(2); // append 2 to the end of the array
list.remove(list.size()-1); // remove the last element from the array
list.size(); // return the number of elements in the array
```


```Python
# Python
l = [] # create an empty dynamic array
l = list() # create an empty dynamic array
l.append(1) # append 1 to the end of the array
l.append(2) # append 2 to the end of the array
l.pop() # remove the last element from the array
# 'list' here is lowercase
# when 'List' is used, it is a type hint
# 'list' is a built-in type in Python
# when using uppercase in python, it is a type hint
# e.g. List[int], List[str], List[List[int]], etc.
```


# Jagged Array

## Summary
- Jagged array is an array of arrays
- Each element of a jagged array can be an array of different sizes
- Jagged array is a good choice when the number of elements in the array is not known in advance

## Jagged Array Definition

```Java
// Java
int[][] jaggedArray = new int[3][];
jaggedArray[0] = new int[3];
jaggedArray[1] = new int[4];
jaggedArray[2] = new int[2];
```

```Python
# Python
jaggedArray = [[0, 1, 2], [3, 4, 5, 6], [7, 8]]
# or append elements to the jagged array
jaggedArray = []
jaggedArray.append([0, 1, 2])
jaggedArray.append([3, 4, 5, 6])
jaggedArray.append([7, 8])
```


## Dynamic Array Implementation

Implement a vector (mutable array with automatic resizing):
 - Practice coding using arrays and pointers, and pointer math to jump to an index instead of using indexing.
 - New raw data array with allocated memory
- can allocate int array under the hood, just not use its features
- start with 16, or if the starting number is greater, use power of 2 - 16, 32, 64, 128
    - size() - number of items
    - capacity() - number of items it can hold
    - is_empty()
    - at(index) - returns the item at a given index, blows up if index out of bounds
    - push(item)
    - insert(index, item) - inserts item at index, shifts that index's value and trailing elements to the right
    - prepend(item) - can use insert above at index 0
    - pop() - remove from end, return value
    - delete(index) - delete item at index, shifting all trailing elements left
    - remove(item) - looks for value and removes index holding it (even if in multiple places)
    - find(item) - looks for value and returns first index with that value, -1 if not found
    - resize(new_capacity) // private function
- when you reach capacity, resize to double the size
- when popping an item, if the size is 1/4 of capacity, resize to half