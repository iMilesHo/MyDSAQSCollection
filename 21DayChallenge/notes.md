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

So reverse the linked list in group should be like (the last group keep the original order):

```python
# 25 reverse nodes in k-group
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

# Day 4

A Toeplitz Matrix is one where the values on every diagonal are the same: Given a 2d matrix (multidimensional array), return true if the input is a Toeplitz matrix and false otherwise.

Example of a valid Toeplitz matrix:

1 2 3 4
5 1 2 3
6 5 1 2
7 6 5 1

```js
function isToeplitz(m) {
  /_ your code here _/;
}
```

```python
class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows, columns = len(matrix), len(matrix[0])

        for r in range(rows):
            for c in range(columns):
                if r!=0 and c!=0 and matrix[r][c]!=matrix[r-1][c-1]:
                    return False
        return True
```

# Day 5

Given a rectangular 2D array of integers, return true if all rows and all columns are monotonically increasing. This means that every successive value along all rows and columns must be AT LEAST as large as what came before.

Example:

[[0, 0, 0, 1],
 [1, 1, 1, 2],
 [2, 3, 4, 5]]

Returns true but this next one returns false.

[[0, 0, 0, 1],
 [1, 1, 3, 2],
 [2, 3, 4, 5]]

```js
function isMatrixMonotonic(matrix) {
  /* your code here */
}
```

```python
def isMatrixMonotonic(matrix: List[List[Int]]) -> bool:
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if i > 0 and j > 0 and matrix[i][j] < matrix[i-1][j] and matrix[i][j] < matrix[i][j-1]:
                return False
    return True
```

# Day 6

Given a matrix that is monotonically increasing along all rows and columns, as well as a value, k, return true if the value exists in the matrix and false otherwise.

Example:

[[0, 0, 0, 1],
 [1, 1, 1, 2],
 [2, 3, 4, 5]]

```python
def findInMonotonic(matrix: List[List[Int]], k: Int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    row, col = rows - 1, 0

    while row >= 0 and col < cols:
        if matrix[row][col] == k:
            return True
        elif matrix[row][col] > k:
            row -= 1
        else:
            col += 1
    return False
```

# Day 7

Given a string, return true if the letters can be re-arranged to make a palindrome using every letter. Otherwise, return false.

function isPalindromeAnagram(word) {
/_ your code here _/
}

```python
def isPalindromeAnagram(word: str) -> bool:
    counter = Counter(word)
    odd_count = 0
    for count in counter.values():
        if count % 2 != 0:
            odd_count += 1
    return odd_count <= 1
```

# Day 8

Given a binary tree, convert this to a doubly linked list in the order of the in-order traversal. This operation should be done in place, not creating any new data structure. You must re-use the node's left pointer as the pointer to the previous node in the list and the right pointer should be the next node in the list.

At the end, return a pointer the first node in the list.

```js

/\*

- You may assume the node class is:
- class Node {
- constructor(value, left = null, right = null) {
-     this.value = value;
-     this.left = left;
-     this.right = right;
- }
- }
  _/
  function tree2list(root) {
  /_ your code here \*/
  }

```

```python
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def convert_to_doubly_linked_list(root: TreeNode) -> TreeNode:
    if not root:
        return None
    first, prev = None, None

    def inorder_traversal(curr: TreeNode):
        nonlocal first, prev
        if not curr:
            return
        inorder_traversal(curr.left)

        if prev:
            prev.right = curr
            curr.left = prev
        else:
            first = curr

        prev = curr

        inorder_traversal(curr.right)
    inorder_traversal(root)
    return first

# Helper function to display the doubly linked list
def print_doubly_linked_list(node):
    while node:
        print(f"{node.value}", end=" <-> " if node.right else "")
        node = node.right
    print()

# Example usage
if __name__ == "__main__":
    # Creating a binary tree:
    #       4
    #      / \
    #     2   5
    #    / \
    #   1   3
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    # Convert to doubly linked list and print
    head = convert_to_doubly_linked_list(root)
    print_doubly_linked_list(head)
```

# Day 9

Implement binary search on an array. Return the index of the value if found and -1 otherwise.

```js
function binarySearch(data, k) {
  /* your code here */
}
```

```python

```
