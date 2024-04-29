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