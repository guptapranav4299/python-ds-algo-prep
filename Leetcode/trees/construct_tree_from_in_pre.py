"""
105. Construct Binary Tree from Preorder and Inorder Traversal

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree
and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]



Constraints:

    1 <= preorder.length <= 3000
    inorder.length == preorder.length
    -3000 <= preorder[i], inorder[i] <= 3000
    preorder and inorder consist of unique values.
    Each value of inorder also appears in preorder.
    preorder is guaranteed to be the preorder traversal of the tree.
    inorder is guaranteed to be the inorder traversal of the tree.

"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_map = {value:index for index, value in enumerate(inorder)}
        global pre_index
        pre_index = 0
        def build_tree_rec(pre, inn, in_start, in_end):
            if in_start>in_end:
                return
            global pre_index
            #get the next element in preorder that will be next parent
            curr = pre[pre_index]
            #create a new node and inxreement the pre_index
            node = TreeNode(curr)
            pre_index+=1
            #if in_start == in_end it means we have single
            if in_start == in_end:
                return node
            else:
                #run the recursion for left and right part of inorder travel
                in_index = in_map[curr]
                node.left = build_tree_rec(pre, inn, in_start, in_index-1)
                node.right = build_tree_rec(pre, inn, in_index+1, in_end)
                return node
        return build_tree_rec(preorder, inorder, 0, len(inorder) -1 )