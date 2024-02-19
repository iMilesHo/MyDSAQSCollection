# String

## Python

Sets in Python are unordered collections of unique elements. They are commonly used in coding interviews for problems involving de-duplication, set operations (like union, intersection, difference), and membership testing, due to their efficient O(1) average time complexity for lookup. Here's an overview of common set methods and operations that are useful to know for coding interviews:

### Creating Sets
- Literal: my_set = {1, 2, 3}
- Constructor: my_set = set([1, 2, 3])
### Basic Operations
- Add an element: .add(elem) - Adds an element to the set.
- Remove an element: .remove(elem) - Removes an element from the set; raises a KeyError if the element is not present.
- Discard an element: .discard(elem) - Removes an element from the set if it is present.
- Pop an element: .pop() - Removes and returns an arbitrary element from the set; raises KeyError if the set is empty.
- Clear the set: .clear() - Removes all elements from the set.
### Set Operations
- Union: set1 | set2 or .union(set2) - Returns a new set with elements from both set1 and set2.
- Intersection: set1 & set2 or .intersection(set2) - Returns a new set with elements common to set1 and set2.
- Difference: set1 - set2 or .difference(set2) - Returns a new set with elements in set1 but not in set2.
- Symmetric Difference: set1 ^ set2 or .- symmetric_difference(set2) - Returns a new set with elements in either set1 or set2 but not in both.
### Membership Testing
- In: elem in set - Checks if elem is a member of the set.
- Not in: elem not in set - Checks if elem is not a member of the set.
### Set Comprehensions
- Similar to list comprehensions but produces a set, which removes duplicate elements. Syntax: {expr for var in iterable if condition}.
### Other Methods
- Subset check: .issubset(set2) or set1 <= set2 - Returns True if set1 is a subset of set2.
- Superset check: .issuperset(set2) or set1 >= set2 - Returns True if set1 is a superset of set2.
- Disjoint check: .isdisjoint(set2) - Returns True if set1 has no elements in common with set2.