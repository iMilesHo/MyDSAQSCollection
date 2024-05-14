# Tree

A tree data structure is a hierachical structure that is used to represent and organize data in a way that is easy to navigate and search.
Applications of trees include:

- file systems (hierarchical file systems)
- HTML DOM (Document Object Model)
- data compression algorithms (Huffman coding)
- Compilers (syntax tree)
- Data indexing (B-trees, AVL trees)

Advantages of trees:

- Efficient data searching
- provides a hierarchical structure that is easy to navigate
- easy to traverse and manipulate using recursion algorithms

Disadvantages of trees:

- manipulation of trees can be complex
- more memory is required to store the tree structure
- trees can be slow to search if the tree is not balanced

## Classic Problems

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorder(root, res)
        return res

    def inorder(self, root, res):
        if root:
            self.inorder(root.left, res)
            res.append(root.val)
            self.inorder(root.right, res)
```

## Tree Traversal

1. Inorder Traversal: left, root, right
2. Preorder Traversal: root, left, right
3. Postorder Traversal: left, right, root

## Cheat Sheet

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        if self.root is None:
            return False
        temp = self.root
        while (temp):
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def BFS(self):
        if self.root is None:
            return []
        queue = []
        visited = []
        node = self.root
        queue.append(node)
        while (len(queue) > 0):
            node = queue.pop(0)
            visited.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return visited
    def BFS_recursive(self):
        if self.root is None:
            return []
        def traverse(queue, visited):
            if len(queue) == 0:
                return visited
            node = queue.pop(0)
            visited.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            return traverse(queue, visited)
        return traverse([self.root], [])


    def DFS_preorder_recursive(self):
        if self.root is None:
            return []
        def traverse(node, visited):
            visited.append(node.value)
            if node.left:
                traverse(node.left, visited)
            if node.right:
                traverse(node.right, visited)
            return visited
        return traverse(self.root, [])

    def DFS_postorder_recursive(self):
        if self.root is None:
            return []
        def traverse(node, visited):
            if node.left:
                traverse(node.left, visited)
            if node.right:
                traverse(node.right, visited)
            visited.append(node.value)
            return visited
        return traverse(self.root, [])

    def DFS_inorder_recursive(self):
        if self.root is None:
            return []
        def traverse(node, visited):
            if node.left:
                traverse(node.left, visited)
            visited.append(node.value)
            if node.right:
                traverse(node.right, visited)
            return visited
        return traverse(self.root, [])

    def DFS_preorder_iterative(self):
        if self.root is None:
            return []
        stack = []
        visited = []
        node = self.root
        stack.append(node)
        while (len(stack) > 0):
            node = stack.pop()
            visited.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return visited
    def DFS_postorder_iterative(self):
        if self.root is None:
            return []
        stack = []
        visited = []
        node = self.root
        stack.append(node)
        while (len(stack) > 0):
            node = stack.pop()
            visited.append(node.value)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return visited[::-1]

    def DFS_inorder_iterative(self):
        if self.root is None:
            return []
        stack = []
        visited = []
        node = self.root
        while (len(stack) > 0 or node):
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                visited.append(node.value)
                node = node.right
        return visited

    def DFS_inorder_recursive1(self):
        if self.root is None:
            return []

        def traverse(visited, node):
            if node.left:
                traverse(visited, node.left)
            visited.append(node.value)
            if node.right:
                traverse(visited, node.right)
            return visited
        return traverse([], self.root)
    #deleting a Node from a BST
    def delete(self, value):
        pass

    # Coverting a Sorted Array to a Balanced BST
    def sortedArrayToBST(self, nums):
        # find the middle element
        # make the middle element the root
        # recursively do the same for the left and right halves

        def helper(left, right):
            if left > right:
                return None
            p = (left + right) // 2
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)

    # Inverting a Binary Tree
    def invertTree(self, root):
        pass

    # Validating a Binary Search Tree
    def isValidBST(self, root):
        pass

```
