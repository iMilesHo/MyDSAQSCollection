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