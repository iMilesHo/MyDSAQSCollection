from typing import List
from traitlets import Int

class LinkListNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

# BFS
def treeHeight(root: LinkListNode):
  if not root:
    return None
  deepest_height = 0
  temp_height = 0
  stack_node = [root]
  while len(stack_node) > 0:
    curr = stack_node.pop()
    temp_height += 1
    if curr.left:
      stack_node.append(curr.left)
    if curr.right:
      stack_node.append(curr.right)
    
    
      
  