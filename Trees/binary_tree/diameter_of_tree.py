class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None


class Solution:
    def height_tree(self, root):
        if root is None:
            return 0

        height_left = self.height_tree(root.left)
        height_right = self.height_tree(root.right)

        return max(height_left, height_right) + 1

    # time - o(n^2)
    def diameter(self, root):
        if root is None:
            return 0

        d1 = 1 + self.height_tree(root.left) + self.height_tree(root.right)
        d2 = self.diameter(root.left)
        d3 = self.diameter(root.right)

        return max((d1, d2, d3))

    def height_max(self, root, ans):
        if root is None:
            return 0
        lh = self.height_max(root.left, ans)
        rh = self.height_max(root.right, ans)

        ans[0] = max(ans[0], 1 + lh + rh)
        return 1 + max(rh, lh)

    # time - 0(n) space - o(h)
    def diameter_efficient(self, root):
        if (root == None):
            return 0
        ans = [-999999999999]  # This will store
        # the final answer
        height_of_tree = self.height_max(root, ans)
        return ans[0]


if __name__ == "__main__":
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)
    root.right.left = Node(40)
    root.right.left.left = Node(50)
    root.right.right = Node(60)
    root.right.right.left = Node(70)

    obj = Solution()
    print(obj.diameter(root))
    print(obj.diameter_efficient(root))
