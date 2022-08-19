class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class Solution:

    # time - o(n) space - o(1)
    def segregate_nodes(self, head):
        es,ee,os,oe = None, None, None, None
        curr = head
        while curr:
            x = curr.key
            if x % 2 == 0:
                if es is None:
                    es = curr
                    ee = es
                else:
                    ee.next = curr
                    ee = ee.next
            else:
                if os is None:
                    os = curr
                    oe = os
                else:
                    oe.next = curr
                    oe = oe.next

            curr = curr.next

        if es is None or os is None:
            return head
        ee.next = os
        oe.next = None
        return es

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
    ans = obj.segregate_nodes(head)
    obj.print_list(ans)
    print()
