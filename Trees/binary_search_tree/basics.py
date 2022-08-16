class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None


class BST:

    def inorder_traversal(self, root):
        if root is None:
            return
        self.inorder_traversal(root.left)
        print(root.key, end="->")
        self.inorder_traversal(root.right)

    # time - o(h) space - o(h)
    def search_recursive(self, root, key):
        if root is None:
            return False
        if key < root.key:
            return self.search_recursive(root.left,key)
        elif key > root.key:
            return self.search_recursive(root.right, key)
        else:
            return True

    # time - o(h) space - o(1)
    def search_iterative(self, root, key):
        while root is not None:
            if root.key == key:
                return True
            elif key < root.key:
                root = root.left
            else:
                root = root.right
        return False

    # time - o(h) space - o(h)
    def insert_recursive(self, root, key):
        if root is None:
            return Node(key)
        if root.key == key:
            return root
        elif root.key > key:
            root.left = self.insert_recursive(root.left, key)
        else:
            root.right = self.insert_recursive(root.right, key)

        return root

    # time - o(h) space - o(1)
    def insert_iterative(self, root, key):
        parent = None
        current = root
        while current is not None:
            parent = current
            if current.key == key:
                return root
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        if parent is None:
            return Node(key)

        if parent.key > key:
            parent.left = Node(key)
        else:
            parent.right = Node(key)
        return root

    # time - o(h) space - o(h)
    def delete_node_recursive(self, root, key):
        if root is None:
            return None
        if key < root.key:
            root.left = self.delete_node_recursive(root.left, key)
        elif key > root.key:
            root.right = self.delete_node_recursive(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.get_successor(root.right, key)
                root.key = successor
                root.right = self.delete_node_recursive(root.right, successor)

        return root

    def get_successor(self, curr, key):
        while curr.left is not None:
            curr = curr.left
        return curr.key

if __name__ == "__main__":
    root = Node(20)
    root.left = Node(10)
    root.left.left = Node(5)
    root.left.right = Node(15)
    root.right = Node(50)
    root.right.left = Node(40)
    root.right.right = Node(60)
    bst = BST()
    bst.inorder_traversal(root)
    print()
    # print(bst.search_recursive(root,40))
    # print(bst.search_recursive(root,70))
    # print("---------------------------")
    # print(bst.search_iterative(root,40))
    # print(bst.search_iterative(root,70))
    print("---------------------------")
    print(bst.inorder_traversal(bst.insert_recursive(root,70)))
    print()
    print("---------------------------")
    print(bst.inorder_traversal(bst.insert_iterative(root,65)))
    print()
    print("---------------------------")
    print(bst.inorder_traversal(bst.delete_node_recursive(root,70)))
    print()
    print("---------------------------")
    print(bst.inorder_traversal(bst.delete_node_recursive(root,50)))
    print()