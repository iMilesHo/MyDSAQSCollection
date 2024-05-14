- What is Trie?

Trie is a tree-like data structure that stores a dynamic set of strings. Tries are used to search for strings in a dataset. The key advantage of using a trie is that it allows for fast lookups in a dataset of strings. Tries are also used in search engines, spell checkers, and other applications that require fast string lookups.

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_name = False
        self.phone_number = None

class PhoneBook:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, name, number):
        node = self.root
        for char in name:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_name = True
        node.phone_number = number

    def search(self, name):
        node = self.root
        for char in name:
            if char not in node.children:
                return "Not found"
            node = node.children[char]
        if node.is_end_of_name:
            return node.phone_number
        return "Not found"

    def update(self, name, number):
        node = self.root
        for char in name:
            if char not in node.children:
                return "Name not found"
            node = node.children[char]
        if node.is_end_of_name:
            node.phone_number = number
            return "Updated successfully"
        return "Name not found"

    def delete(self, node, name, depth=0):
        if node is None:
            return None, False

        if depth == len(name):
            if node.is_end_of_name:
                node.is_end_of_name = False
                if not node.children:
                    return None, True
                return node, False
            return node, False

        char = name[depth]
        node.children[char], should_delete = self.delete(node.children[char], name, depth + 1)

        if should_delete:
            del node.children[char]
            if not node.children and not node.is_end_of_name:
                return None, True
        return node, False

    def delete_entry(self, name):
        self.root, deleted = self.delete(self.root, name)
        return "Deleted successfully" if deleted else "Name not found"

# Example usage
phone_book = PhoneBook()
phone_book.insert("Alice", "1234567890")
print(phone_book.search("Alice"))  # Output: 1234567890
print(phone_book.update("Alice", "0987654321"))  # Output: Updated successfully
print(phone_book.delete_entry("Alice"))  # Output: Deleted successfully
print(phone_book.search("Alice"))  # Output: Not found
```

# Hash Table

- key-value pair data structure
- used for efficient search, insert, and delete operations
- typically offers O(1) time complexity for these operations
- In Python, hash tables are implemented using dictionaries (dict class)
- different key will have different unique bucket index but collision can occur via hash function

## Key features of hash table

- Hash function: converts the key into an index
- Bucket: a slot to store multiple entries in the case of collision
- Collision handling:
  - chaining: store multiple entries in the same bucket
  - open addressing: find another empty bucket to store the entry

## Basic operations with Python dictionary

- please refer to the Dictionary.md file

## handling collision

- chaining: store multiple entries in the same bucket
- open addressing: find another empty bucket to store the entry
  - linear probing: check the next bucket
  - quadratic probing: check the next bucket with a quadratic function
  - double hashing: check the next bucket with a second hash function

## Dictionary order

- Python 3.7+: insertion order is preserved

## Memory usage

- python dictionary is designed for speed

## Set

- set in Python is implemented using a hash table

## Common Pitfalls

- mutable objects should not be used as keys

```python
# Example
my_dict = {}
my_list = [1, 2, 3]
my_dict[my_list] = "value"  # TypeError: unhashable type: 'list'

# Solution
my_dict[tuple(my_list)] = "value"

# or
my_dict[frozenset(my_list)] = "value"
```

- use .get() method to avoid KeyError

# Cheat Sheet

```python
# Item In common
def item_in_common(list1, list2):
    return list(set(list1) & set(list2))

# find duplicates
def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

# first non-repeating character
def first_non_repeating_char(s):
    seen = set()
    dupliacted = set()
    for i in s:
        if i in seen:
            dupliacted.add(i)
        else:
            seen.add(i)
    for i in s:
        if i not in dupliacted:
            return i
    return None
# or
def first_non_repeating_char(s):
    seen = {}
    for i in s:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1
    # the order of the dictionary is preserved in Python 3.7+
    for i in s:
        if seen[i] == 1:
            return i
    return None

# Group Anagrams
def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        key = "".join(sorted(s))
        if key not in anagrams:
            anagrams[key] = []
        anagrams[key].append(s)
    return list(anagrams.values())

# Two sum
def two_sum(nums, target):
    complementarys = {}
    for i in range(len(nums)):
        complementary = target - nums[i]
        if complementary not in complementarys:
            complementarys[nums[i]] = i
        else:
            return [complementarys[complementary],i]
    return []
#or
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
    return []

# target subarray sum
def target_subarray_sum(nums, target):
    seen = {}
    current_sum = 0
    for i, num in enumerate(nums):
        current_sum += num
        if current_sum == target:
            return nums[:i + 1]
        if current_sum - target in seen:
            return nums[seen[current_sum - target] + 1:i + 1]
        seen[current_sum] = i
    return []

```
