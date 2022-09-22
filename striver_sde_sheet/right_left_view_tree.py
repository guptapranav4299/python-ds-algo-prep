"""
199. Binary Tree Right Side View

Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Input: root = [1,null,3]
Output: [1,3]

Input: root = []
Output: []

Constraints:
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        def helper(root, level):
            if root is None:
                return None
            if len(ls) == level:
                ls.append(root.val)
            helper(root.right, level + 1)
            helper(root.left, level + 1)
        helper(root,  0)
        return ls

    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        ls = []
        def helper(root, level):
            if root is None:
                return None
            if len(ls) == level:
                ls.append(root.val)
            helper(root.left, level + 1)
            helper(root.right, level + 1)
        helper(root,  0)
        return ls