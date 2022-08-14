from collections import deque


class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None


class IterativeTraversals:
    # time - o(n) space - o(n)
    def inorder_traversal(self, root):
        if root is None:
            return
        st = deque()
        curr = root

        while curr is not None:
            st.append(curr)
            curr = curr.left
        while len(st) > 0:
            curr = st.pop()
            print(curr.key,end="->")
            curr = curr.right
            while curr is not None:
                st.append(curr)
                curr = curr.left

    def pre_order_traversal(self,root):
        if root is None:
            return
        st = [root]
        while len(st) > 0:
            curr = st.pop()
            print(curr.key, end="->")
            if curr.right is not None:
                st.append(curr.right)
            if curr.left is not None:
                st.append(curr.left)

    # time - o(n) space - o(n)
    def postorder_traversal(self,root):
        if root is None:
            return
        s1 = []
        s2 = []
        s1.append(root)
        while s1:
            curr = s1.pop()
            s2.append(curr)
            if curr.left:
                s1.append(curr.left)
            if curr.right:
                s1.append(curr.right)

        while s2:
            node = s2.pop()
            print(node.key,end="->")

    def level_order_traversal(self, root):
        if root is None:
            return
        q = deque()
        q.append(root)
        while len(q) > 0:
            curr = q.popleft()
            print(curr.key,end="->")
            if curr.left is not None:
                q.append(curr.left)
            if curr.right is not None:
                q.append(curr.right)


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.right = Node(50)
    traversal = IterativeTraversals()
    print("-----------In Order Traversal-------------")
    traversal.inorder_traversal(root)
    print()
    print("-----------Post Order Traversal-------------")
    traversal.postorder_traversal(root)
    print()
    print("-----------Pre Order Traversal-------------")
    traversal.pre_order_traversal(root)
    print()
    print("-----------Level Order Traversal-------------")
    traversal.level_order_traversal(root)
    print()
