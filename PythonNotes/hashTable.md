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