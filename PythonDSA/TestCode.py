from typing import List, Optional
from traitlets import Int
from collections import Counter, defaultdict, deque

result = []
q = deque()
if len(q) == 0:
    print("Empty")
q.append(1)
print(q.popleft())
print(q)