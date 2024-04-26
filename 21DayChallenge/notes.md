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

# Day 2

Given a 2D rectangular matrix, return all of the values in a single, linear array in spiral order. Start at (0, 0) and first include everything in the first row. Then down the last column, back the last row (in reverse), and finally up the first column before turning right and continuing into the interior of the matrix.

For example:

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Returns:

[1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

function spiralTraversal(matrix) {
/_ your code here _/
}

```python
def spiralTraversal(matrix: List[List[Int]]) -> List[Int]:
    if not matrix and not matrix[0]:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result
```

# Day 3

Given a linked list, reverse groups of k nodes. These groups will remain in order themselves. For example, if we perform this operation with k=2 on the following list:

1 -> 2 -> 3 -> 4-> 5

The result will be:

2 -> 1 -> 4 -> 3 -> 5

Once again, this should be done in-place, just re-assigning the next pointers in the nodes and returning the new head. The head parameter will be a list of some length (possibly zero) and k will be a positive integer.

```js
/*
 * You may assume the node class is:
 * class LLNode {
 *   constructor(value, next = null) {
 *     this.value = value;
 *     this.next = next;
 *   }
 * }
 */
function reverseInGroupsOfK(head, k) {
  /* your code here */
}
```

At first, reverse the whole linkedlist should be like:

```python
class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def reverseLinkedList(head):
    if not head and not head.next:
        return head

    pre = None
    mid = head
    after = head.next

    while mid:
        after = mid.next
        mid.next = pre
        pre = mid
        mid = after

    return pre
```

So reverse the linked list in group should be like:

```python
def reverseInGroupsOfK(head, k):
    if not head and not head.next:
        return head

    pre = None
    mid = head

    newHead = None
    group_trail = head

    count = 0

    while mid:
        after = mid.next
        mid.next = pre
        pre = mid
        mid = after

        count += 1

        if count == k:
            newHead = pre
        if count % k = 0 or not mid:
            pre = group_trail
            group_trail = mid

    return newHead

def reverseLinkedList(head, trail):
    if not head and not head.next:
        return head

    pre = None
    mid = head
    after = head.next

    while mid == trail.next:
        after = mid.next
        mid.next = pre
        pre = mid
        mid = after

    return pre, head
```
