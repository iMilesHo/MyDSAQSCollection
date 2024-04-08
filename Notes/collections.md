# python collections

## collections module
The `collections` module provides alternatives to built-in container data types such as `dict`, `list`, `set`, and `tuple`.

### Counter
The `Counter` class is a subclass of `dict` that counts hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts as dictionary values.

```Python
from collections import Counter

# Create a Counter object
c = Counter('gallahad')
print(c) # Output: Counter({'a': 3, 'l': 2, 'g': 1, 'h': 1, 'd': 1})
# Get the count of a specific element
print(c['a']) # Output: 3

# Create a Counter object from a list
c = Counter(['eggs', 'ham'])
print(c) # Output: Counter({'eggs': 1, 'ham': 1})
```



