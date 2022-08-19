class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class Solution:
    def pairwise_swap_naive(self, head):
        curr = head
        while curr and curr.next:
            curr.key, curr.next.key = curr.next.key, curr.key
            curr = curr.next.next
        return head

    def pairwise_swap_efficient(self, head):
        if head is None or head.next is None:
            return head
        curr = head.next.next
        prev = head
        head = head.next
        head.next = prev
        while curr and  curr.next:
            prev.next = curr.next
            prev = curr
            n = curr.next.next
            curr.next.next = curr
            curr = n
        prev.next = curr
        return head

    def print_list(self, head):
        temp = head
        while temp:
            print(temp.key, end="->")
            temp = temp.next


if __name__ == "__main__":
    head = Node(10)
    head.next = Node(25)
    head.next.next = Node(30)
    head.next.next.next = Node(45)
    head.next.next.next.next = Node(56)
    head.next.next.next.next.next = Node(65)
    obj = Solution()
    # ans = obj.pairwise_swap_naive(head)
    # obj.print_list(ans)
    # print()
    ans1 = obj.pairwise_swap_naive(head)
    obj.print_list(ans1)
    print()