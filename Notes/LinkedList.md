# LinkedList

## Definition
- a linear data structure
- stored in nodes: a value and a pointer to the next node
- head and tail nodes

## Advantages
- Dynamic size
- Ease of insertion/deletion without reallocation, time complexity is O(1)

## Disadvantages
- Random access is not allowed. We have to access elements sequentially starting from the first node.
- Extra memory space is required for a pointer.
- Not cache friendly. Since the elements are not stored in contiguous memory locations, the CPU cache is not utilized effectively.
- Complexity of searching is O(n)

## Types
- Singly linked list: Each node has a value and a pointer to the next node.
- Doubly linked list: Each node has a value, a pointer to the next node, and a pointer to the previous node.
- Circular linked list: The last node points to the first node.

## Python Implementation
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

## Basic Operations
- Insertion
- Deletion
- Traversal
- Search
- Length

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def delete(self, val):
        temp = self.head
        if temp is not None:
            if temp.val == val:
                self.head = temp.next
                temp = None
                self.size -= 1
                return
        while temp is not None:
            if temp.val == val:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None
        self.size -= 1
    
    def search(self, val):
        temp = self.head
        while temp is not None:
            if temp.val == val:
                return True
            temp = temp.next
        return False
    
    def length(self):
        return self.size
    
    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.val)
            temp = temp.next
```

## Problems



