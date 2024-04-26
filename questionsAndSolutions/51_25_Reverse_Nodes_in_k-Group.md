# 25. Reverse Nodes in k-Group

## My solution

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (not head and not head.next) or k == 1:
            return head

        # get the length of the linked list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        pre = None
        mid = head

        newHead = None
        group_trail = head
        next_group_trail = None

        count = 0

        last_group_count = length//k * k


        while mid and count < last_group_count:
            after = mid.next
            mid.next = pre
            pre = mid
            mid = after

            count += 1
            if count == k:
                newHead = pre
            if count % k == 0:
                if group_trail == head:
                    head = pre
                    next_group_trail = mid
                else:
                    group_trail.next = pre
                    group_trail = next_group_trail
                    group_trail.next = None
                    pre = None
                    next_group_trail = mid

        # if the last group is less than k
        group_trail.next = mid

        return newHead
```
