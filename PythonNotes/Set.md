# String

## Python

Sets in Python are unordered collections of unique elements. They are commonly used in coding interviews for problems involving de-duplication, set operations (like union, intersection, difference), and membership testing, due to their **efficient O(1) average time complexity for lookup**. Here's an overview of common set methods and operations that are useful to know for coding interviews:

### Creating Sets

- Literal: my_set = {1, 2, 3}
- Constructor: my_set = set([1, 2, 3])

### Basic Operations

- Add an element: .add(elem) - Adds an element to the set.

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
```

- Remove an element: .remove(elem) - Removes an element from the set; raises a KeyError if the element is not present.

```python
my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

my_set.remove(2)  # KeyError: 2 not in set
```

- Discard an element: .discard(elem) - Removes an element from the set if it is present.

```python
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}

my_set.discard(2)
print(my_set)  # Output: {1, 3}
```

- Pop an element: .pop() - Removes and returns an arbitrary element from the set; raises KeyError if the set is empty.

```python
my_set = {1, 2, 3}
print(my_set.pop())  # Output: 1
print(my_set)  # Output: {2, 3}
```

- Clear the set: .clear() - Removes all elements from the set.

### Set Operations

- Union: set1 | set2 or .union(set2) - Returns a new set with elements from both set1 and set2.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1 | set2
print(set3)  # Output: {1, 2, 3, 4, 5}

set3 = set1.union(set2)
print(set3)  # Output: {1, 2, 3, 4, 5}
print(set1)  # Output: {1, 2, 3}
```

- Intersection: set1 & set2 or .intersection(set2) - Returns a new set with elements common to set1 and set2.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1 & set2
print(set3)  # Output: {3}

set3 = set1.intersection(set2)
print(set3)  # Output: {3}
print(set1)  # Output: {1, 2, 3}
```

- Difference: set1 - set2 or .difference(set2) - Returns a new set with elements in set1 but not in set2.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1 - set2
print(set3)  # Output: {1, 2}

set3 = set1.difference(set2)
print(set3)  # Output: {1, 2}
print(set1)  # Output: {1, 2, 3}
```

- Symmetric Difference: set1 ^ set2 or .symmetric_difference(set2) - Returns a new set with elements in either set1 or set2 but not in both.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1 ^ set2
print(set3)  # Output: {1, 2, 4, 5}

set3 = set1.symmetric_difference(set2)
print(set3)  # Output: {1, 2, 4, 5}
print(set1)  # Output: {1, 2, 3}
```

### Membership Testing

- In: elem in set - Checks if elem is a member of the set.

```python
my_set = {1, 2, 3}
print(1 in my_set)  # Output: True
print(4 in my_set)  # Output: False
```

- Not in: elem not in set - Checks if elem is not a member of the set.

```python
my_set = {1, 2, 3}
print(1 not in my_set)  # Output: False
print(4 not in my_set)  # Output: True
```

### Set Comprehensions

- Similar to list comprehensions but produces a set, which removes duplicate elements. Syntax: {expr for var in iterable if condition}.

### Other Methods

- Subset check: .issubset(set2) or set1 <= set2 - Returns True if set1 is a subset of set2.

```python
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True
print(set1 <= set2)  # Output: True
```

- Superset check: .issuperset(set2) or set1 >= set2 - Returns True if set1 is a superset of set2.

```python
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True
print(set1 >= set2)  # Output: True
```

- Disjoint check: .isdisjoint(set2) - Returns True if set1 has no elements in common with set2.

```python
set1 = {1, 2}
set2 = {3, 4}
print(set1.isdisjoint(set2))  # Output: True
```
