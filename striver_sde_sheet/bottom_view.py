"""
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.

                      20
                    /    \
                  8       22
                /   \        \
              5      3       25
                    /   \
                  10    14

For the above tree, the bottom view is 5 10 3 14 25.
If there are multiple bottom-most nodes for a horizontal distance from root, then print the later
one in level traversal. For example, in the below diagram, 3 and 4 are both the bottommost nodes
at horizontal distance 0, we need to print 4.


                      20
                    /    \
                  8       22
                /   \     /   \
              5      3 4     25
                     /    \
                 10       14

For the above tree the output should be 5 10 4 14 25.

Your Task:
This is a functional problem, you don't need to care about input, just complete the function
bottomView() which takes the root node of the tree as input and returns an array
containing the bottom view of the given tree.

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= Number of nodes <= 105
1 <= Data of a node <= 105

"""


class Solution:
    def bottomView(self, root):
        # code here
        q = [[root, 0]]
        dict = {}
        while q:
            node, level = q.pop(0)
            dict[level] = node.data
            if node.left:
                q.append([node.left, level - 1])
            if node.right:
                q.append([node.right, level + 1])
        ans = []
        dict = sorted(dict.items())
        for i in range(len(dict)):
            ans.append(dict[i][1])
        return ans