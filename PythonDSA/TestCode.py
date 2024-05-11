from typing import List, Optional
from traitlets import Int

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def convert_to_doubly_linked_list(root: TreeNode) -> TreeNode:
    if not root:
        return None
    head, prev = None, None

    def inorder_traversal(curr: TreeNode):
        if not curr:
            return curr
        inorder_traversal(curr.left)

        if not prev:
            head = curr
        else:
            prev.right = curr
            curr.left = prev
        
        prev = curr
        inorder_traversal(curr.right)
    inorder_traversal(root)
    return head

