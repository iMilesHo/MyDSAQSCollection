# 206. Reverse Linked List

## Python Solution

### My Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_before = head
        
        slicde_pointer = head
        if slicde_pointer is None:
            return None
        elif slicde_pointer.next is None:
            return slicde_pointer

        previous = slicde_pointer
        slicde_pointer = slicde_pointer.next
        after = slicde_pointer.next
                
        while slicde_pointer is not None:
            slicde_pointer.next = previous
            previous = slicde_pointer
            slicde_pointer = after
            if slicde_pointer is None:
                break
            after = slicde_pointer.next
        
        head_before.next = None
        return previous
```

#### Notes
- In general, the official variable names of the linked list are `current`, `previous`, and `next`.

### Leetcode Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        cur=head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        head=prev
        return head

```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
            
        return prev
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next :
            return head
        
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
            
        return prev
```

