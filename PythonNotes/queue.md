# Queue in Python

- First In First Out (FIFO) data structure
- linked list implementation
- fixed-size array implementation

## Queue Operations

- `enqueue(item)`: add an item to the queue
- `dequeue()`: remove the first item from the queue
- `peek()`: return the first item in the queue
- `is_empty()`: check if the queue is empty
- `size()`: return the number of items in the queue

## Queue Implementation

```python
# using collections.deque
from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, item):
        self.container.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.container.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty queue")
        return self.container[0]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

# Example of using the Queue
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())  # Output: 1
print(q.peek())     # Output: 2
print(q.size())     # Output: 2
```

## Practice uses of Queues

Queue are useful in many scenarios, such as:

- Breadth First Search (BFS) algorithm: to hold a list of nodes to visit
- Concurrency Operations: to manage tasks in a multi-threaded environment
- Buffering: to store data before processing

## Exercise

```python
from collections import deque

def generate_binary_numbers(n):
    result = []
    q = deque()
    q.append("1")

    for _ in range(n):
        front = q.popleft()
        result.append(front)
        q.append(front + "0")
        q.append(front + "1")

    return result

# Example usage
print(generate_binary_numbers(5))  # Output: ['1', '10', '11', '100', '101']
```

## Cheat Sheet

```python
#using list
queue = []
# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
# dequeue
queue.pop(0)  # Output: 1
# peek
queue[0]  # Output: 2
# is_empty
len(queue) == 0

# using collections.deque
from collections import deque
queue = deque()
# enqueue
queue.append(1)
queue.append(2)
queue.append(3)
# dequeue
queue.popleft()  # Output: 1
#peek
queue[0]  # Output: 2
# is_empty
len(queue) == 0

# using two stacks
stack1 = []
stack2 = []
# enqueue
stack1.append(1)
stack1.append(2)
stack1.append(3)
# dequeue
if not stack2:
    while stack1:
        stack2.append(stack1.pop())
stack2.pop()  # Output: 1
while stack2:
    stack1.append(stack2.pop())
```
