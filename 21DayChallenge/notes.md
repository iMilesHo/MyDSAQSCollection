# Day 1

Given a linked list, delete the middle node. If the list is even length, delete the node at the start of the second half of the list.

```python
# definition of ListNode
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_middle_node(head: ListNode) -> ListNode:
    if not head or not head.next:
        return None
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev.next = slow.next
    return head
# test
# [1, 2, 3, 4, 5] -> [1, 2, 4, 5]
# [1, 2, 3, 4, 5, 6] -> [1, 2, 3, 5, 6]


```
