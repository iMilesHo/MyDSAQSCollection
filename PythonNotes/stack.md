# Stack in Python
- Last In First Out (LIFO) data structure

## Stack Operations
- `push(item)`: add an item to the stack
- `pop()`: remove the top item from the stack
- `peek()`: return the top item in the stack
- `is_empty()`: check if the stack is empty
- `size()`: return the number of items in the stack

## Stack Implementation
```python
class Stack:
    def __init__(self):
        self.container = []

    def push(self, item):
        self.container.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.container.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

# Example of using the Stack
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())  # Output: 3
print(s.peek())  # Output: 2
print(s.size())  # Output: 2
```

## Practice uses of Stacks
- Function call stack: to store function calls in memory
- Expression evaluation: to convert infix expressions to postfix
- Undo mechanism: to store the history of actions for undoing
- Depth First Search (DFS) algorithm: to hold a list of nodes to visit
- Syntax parsing: to check the validity of parentheses in expressions

