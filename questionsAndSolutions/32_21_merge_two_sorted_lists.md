# 21. Merge Two Sorted Lists


```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        pointor1 = list1
        pointor2 = list2
        head = list1
        if pointor1.val <= pointor2.val:
            head = pointor1
            pointor1 = pointor1.next
        else:
            head = pointor2
            pointor2 = pointor2.next
        temp = head
        while pointor1 and pointor2:
            if pointor1.val <= pointor2.val:
                temp.next = pointor1
                temp = pointor1
                pointor1 = pointor1.next
            else:
                temp.next = pointor2
                temp = pointor2
                pointor2 = pointor2.next
        
        if pointor1:
            temp.next = pointor1
        if pointor2:
            temp.next = pointor2
        return head



        
```
