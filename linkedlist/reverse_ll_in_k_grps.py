class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class Solution:
    # time -o(n) , space - o(n/k)
    def reverse_k_grp_recursive(self, head, k):
        curr = head
        prev, n = None, None
        count = 0
        while curr and count < k:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
            count += 1

        if n:
            rem_head = self.reverse_k_grp_recursive(curr, k)
            head.next = rem_head

        return prev

    def print_list(self, head):
        temp = head
        while temp:
            print(temp.key, end="->")
            temp = temp.next

    def reverse_k_grp_iterative(self, head, k):
        curr = head
        prev_first = None
        first_pass = True

        while curr:
            first, prev = curr, None
            count = 0
            while curr and count < k:
                n = curr.next
                curr.next = prev
                prev = curr
                curr = n
                count += 1
            if first_pass:
                head = prev
                first_pass = False
            else:
                prev_first.next = prev
            prev_first = first
        return head


if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)
    obj = Solution()
    obj.print_list(head)
    print()
    print("---------------------")
    # head = obj.reverse_k_grp_recursive(head, 3)
    head = obj.reverse_k_grp_iterative(head, 3)
    obj.print_list(head)
    print()
"""
10->20->30->40->50->60->
---------------------
30->20->10->60->50->40->

10->20->30->40->50->60->
---------------------
30->20->10->60->50->40->
"""