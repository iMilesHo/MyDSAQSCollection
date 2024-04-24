from typing import List

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
def build_linked_list(arr: List[int]) -> ListNode:
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

def print_linked_list(head: ListNode) -> None:
    current = head
    while current:
        print(current.val, end=' ')
        current = current.next
    print()

head = build_linked_list([1, 2, 3, 4, 5])
print_linked_list(head)
head = delete_middle_node(head)
print_linked_list(head)

head = build_linked_list([1, 2, 3, 4, 5, 6])
print_linked_list(head)
head = delete_middle_node(head)
print_linked_list(head)
