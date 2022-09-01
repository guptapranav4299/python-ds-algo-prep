class Node:
    def __init__(self, k):
        self.key=k
        self.next = None

class Solution:
    def print_list(self, head):
        if head is None:
            return
        print(head.key, end=" ")
        curr = head.next
        while curr != head:
            print(curr.key, end=" ")
            curr = curr.next

    def insert_begining(self, head, item):
        temp = Node(item)
        if head is None:
            temp.next = temp
            return temp
        else:
            temp.next = head.next
            head.next = temp

        head.key,temp.key = temp.key,head.key
        return head


if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = head
    obj = Solution()
    obj.insert_begining(head, 5)
    obj.print_list(head)
    print()