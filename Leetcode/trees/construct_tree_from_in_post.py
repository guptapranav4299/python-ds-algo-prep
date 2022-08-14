"""
106. Construct Binary Tree from Inorder and Postorder Traversal

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree
and postorder is the postorder traversal of the same tree, construct and return the binary tree.

Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]



Constraints:

    1 <= inorder.length <= 3000
    postorder.length == inorder.length
    -3000 <= inorder[i], postorder[i] <= 3000
    inorder and postorder consist of unique values.
    Each value of postorder also appears in inorder.
    inorder is guaranteed to be the inorder traversal of the tree.
    postorder is guaranteed to be the postorder traversal of the tree

"""

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_map = {value:index for index, value in enumerate(inorder)}
        global pre_index
        pre_index = len(inorder) - 1
        def build_tree_rec(post, inn, in_start, in_end):
            if in_start>in_end:
                return
            global pre_index
            #get the next element in preorder that will be next parent
            curr = post[pre_index]
            #create a new node and inxreement the pre_index
            node = TreeNode(curr)
            pre_index-=1
            #if in_start == in_end it means we have single
            if in_start == in_end:
                return node
            else:
                #run the recursion for left and right part of inorder travel
                in_index = in_map[curr]
                node.right = build_tree_rec(post, inn, in_index+1, in_end)
                node.left = build_tree_rec(post, inn, in_start, in_index-1)
                return node
        return build_tree_rec(postorder, inorder, 0, len(inorder) -1 )