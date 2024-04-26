from typing import List
from traitlets import Int

class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def reverseInGroupsOfK(head, k):
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

def printList(head):
    while head:
        print(head.value, end = " ")
        head = head.next
    print()

def createList(arr: List[int]) -> Node:
    head = Node(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next
    return head

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    head = createList(arr)
    printList(head)
    head = reverseInGroupsOfK(head, 1)
    printList(head)
