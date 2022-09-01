from collections import deque
from math import inf


class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None


pre_idx = 0
mp = {}


class Traversal:
    calls = 0

    def inorder_traversal(self, root):
        if root is not None:
            if root.left is not None:
                self.inorder_traversal(root.left)
                self.calls += 1
            print(root.key, end="->")
            if root.right is not None:
                self.calls += 1
                self.inorder_traversal(root.right)

    def in_order_traversal_basic(self, root):
        if root is not None:
            self.in_order_traversal_basic(root.left)
            self.calls += 1
            print(root.key, end="->")
            self.in_order_traversal_basic(root.right)
            self.calls += 1

    def pre_order_traversal(self, root):
        if root is not None:
            print(root.key, end="->")
            self.pre_order_traversal(root.left)
            self.pre_order_traversal(root.right)

    def post_order_traversal(self, root):
        if root is not None:
            self.post_order_traversal(root.left)
            self.post_order_traversal(root.right)
            print(root.key, end="->")

    def height_tree(self, root):
        if root is None:
            return 0

        height_left = self.height_tree(root.left)
        height_right = self.height_tree(root.right)

        return max(height_left, height_right) + 1

    def size_tree(self, root):
        if root is None:
            return -1

        height_left = self.size_tree(root.left)
        height_right = self.size_tree(root.right)

        return height_left + height_right + 1

    def max_element_tree(self, root):
        if root is None:
            return -inf

        element_left = self.max_element_tree(root.left)
        element_right = self.max_element_tree(root.right)

        return max((element_left, element_right, root.key))

    def is_balanced_tree(self, root):
        if self.is_balanced_tree_recursive(root):
            return True
        else:
            return False

    def is_balanced_tree_recursive(self, root):
        if root is None:
            return 0
        lh = self.is_balanced_tree_recursive(root.left)
        if lh == -1:
            return -1
        rh = self.is_balanced_tree_recursive(root.right)
        if rh == -1:
            return -1
        if abs(lh - rh) > 1:
            return -1
        return max(lh, rh) + 1

    def max_width(self, root):
        if root is None:
            return 0
        q = deque()
        q.append(root)
        res = 0
        while q:
            count = len(q)
            for i in range(count):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res = max(res, count)
        return res

    def buildTree(self, inorder, preorder):
        global mp
        for i in range(len(io)):
            mp[inorder[i]] = i
        root = self.tree_from_in_pre(preorder, inorder, 0, len(inorder) - 1)
        self.printInorder(root)

    def tree_from_in_pre(self, pre, io, isidx, ieidx):
        if isidx > ieidx:
            return None

        global pre_idx
        root = Node(pre[pre_idx])
        pre_idx += 1

        if isidx == ieidx:
            return root

        i = mp[root.key]
        root.left = self.tree_from_in_pre(pre, io, isidx, i - 1)
        root.right = self.tree_from_in_pre(pre, io, i + 1, ieidx)
        return root

    def printInorder(self, node):
        if node is None:
            return

        # first recur on left child
        self.printInorder(node.left)

        # then print the data of node
        print(node.key, end=' ')

        # now recur on right child
        self.printInorder(node.right)

    def search_in_tree(self, root, key):
        if root is None:
            return False
        if key == root.key:
            return True
        elif self.search_in_tree(root.left, key):
            return True
        elif self.search_in_tree(root.right, key):
            return True
        else:
            return False


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)

    traversal = Traversal()
    # print("--------Inorder Traversal----------")
    # traversal.inorder_traversal(root)
    # print()
    # print("calls", traversal.calls)

    # print("--------Inorder Traversal----------")
    # traversal.in_order_traversal_basic(root)
    # print()
    # print("calls", traversal.calls)
    # print("--------Preorder Traversal----------")
    # traversal.pre_order_traversal(root)
    # print()
    # print("--------Postorder Traversal----------")
    # traversal.post_order_traversal(root)
    # print("--------Height of Tree----------")
    # print(traversal.height_tree(root))
    # print("--------Size of Tree----------")
    # print(traversal.size_tree(root))
    # print("--------Max Element of Tree----------")
    # print(traversal.max_element_tree(root))
    # print("--------is Balanced Tree----------")
    # print(traversal.is_balanced_tree(root))
    # print("--------Max Width Tree----------")
    # print(traversal.max_width(root))
    pre = [10, 20, 30, 40, 50]
    io = [20, 10, 40, 30, 50]
    # traversal.buildTree(io,pre)
    # print(traversal.tree_from_in_pre(pre,io,0,4))
    print(traversal.search_in_tree(root, 50))
