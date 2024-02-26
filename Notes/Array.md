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

# Python Array

## Adding Elements
- .append(element): Adds a single element to the end of the list.
```python
l = [1, 2, 3]
l.append(4)
print(l) # [1, 2, 3, 4]
```
- .extend(iterable): Extends the list by appending elements from the iterable.
```python
l = [1, 2, 3]
l.extend([4, 5, 6])
print(l) # [1, 2, 3, 4, 5, 6]
```
- .insert(index, element): Inserts an element at a specified index.
```python
l = [1, 2, 3]
l.insert(1, 5)
print(l) # [1, 5, 2, 3]
```
## Removing Elements
- .remove(element): Removes the first occurrence of a value.
```python
l = [1, 2, 3, 4, 3]
l.remove(3)
print(l) # [1, 2, 4, 3]
```
- .pop([index]): Removes and returns an element at the given index (last element if index is not provided).
```python
l = [1, 2, 3, 4]
print(l.pop()) # 4
print(l) # [1, 2, 3]

print(l.pop(1)) # 2
print(l) # [1, 3]
```
- .clear(): Removes all items from the list.
```python
l = [1, 2, 3]
l.clear()
print(l) # []
```

## Finding Elements
- .index(element, [start, [end]]): Returns the index of the first occurrence of a value.
```python
l = [1, 2, 3, 4, 3]
print(l.index(3)) # 2

# search for 3 starting from index 3
print(l.index(3, 3)) # 4

# search for 3 between index 3 and 4
print(l.index(3, 3, 5)) # 4
```
- .count(element): Returns the number of occurrences of a value.
```python
l = [1, 2, 3, 4, 3]
print(l.count(3)) # 2
```
## Ordering and Sorting
- .sort([key=None, reverse=False]): Sorts the items of the list in place (the arguments can be used for custom sort orders).
```python
l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
l.sort() # in place sorting, non-decreasing order
l.sort(reverse=True) # in place sorting, non-increasing order
l.sort(key=lambda x: x%3) # in place sorting, based on the remainder of the elements when divided by 3
```
- .reverse(): Reverses the elements of the list in place.
```python
l = [1, 2, 3, 4, 5]
l.reverse()
print(l) # [5, 4, 3, 2, 1]
```
## Copying
- .copy(): Returns a shallow copy of the list.
```python
l = [1, 2, 3]
l2 = l.copy()
l2[0] = 4
print(l) # [1, 2, 3]
print(l2) # [4, 2, 3]
```

## Other Commonly Used in Interviews
- len(list): Returns the number of items in the list.
```python
l = [1, 2, 3, 4, 5]
print(len(l)) # 5
```

- max(list): Returns the largest item in an iterable or the largest of two or more arguments.
```python
l = [1, 2, 3, 4, 5]
print(max(l)) # 5
```
- min(list): Returns the smallest item in an iterable or the smallest of two or more arguments.
```python
l = [1, 2, 3, 4, 5]
print(min(l)) # 1
```
- sum(list): Sums the items of an iterable from left to right and returns the total.
```python
l = [1, 2, 3, 4, 5]
print(sum(l)) # 15
```
## List comprehension
`[expression for item in iterable if condition]` for generating a new list based on existing lists, often used for filtering and transforming elements.
```python
l = [1, 2, 3, 4, 5]
l2 = [x**2 for x in l if x%2==0] # if x is even, then square x
print(l2) # [4, 16]
```

## Slicing
`list[start:stop:step]` to make a new list out of an existing list by specifying start, stop, and step indices.
```python
l = [1, 2, 3, 4, 5]
print(l[1:3]) # [2, 3]
print(l[::2]) # [1, 3, 5]
```