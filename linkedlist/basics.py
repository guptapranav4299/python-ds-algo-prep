class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


class Operations:

    def print_list(self, head):
        temp = head
        while temp != None:
            print(temp.key, end="->")
            temp = temp.next

    def search_in_list(self, head, item):
        curr = head
        pos = 1
        while curr is not None:
            if curr.key == item:
                return pos
            pos += 1
            curr = curr.next
        return -1

    def length_list(self, head):
        curr = head
        size = 1
        while curr is not None:
            size += 1
            curr = curr.next
        return size

    def insert_start(self, head, item):
        temp = Node(item)
        temp.next = head
        return temp

    def insert_end(self, head, item):
        if head is None:
            return Node(item)
        curr = head
        while curr.next is not None:
            curr = curr.next
        temp = Node(item)
        curr.next = temp
        return head

    def insert_at_position(self, head, item, pos):
        temp = Node(item)
        if pos == 1:
            temp.next = head
            return temp
        cur = head

        for i in range(pos - 2):
            cur = cur.next
            if cur is None:
                return head

        temp.next = cur.next
        cur.next = temp
        return head

    def delete_first(self, head):
        if head is None:
            return None
        else:
            return head.next

    def delete_last(self, head):
        if head is None:
            return None
        if head.next is None:
            return None

        curr = head
        while curr.next.next is not None:
            curr = curr.next

        curr.next = None
        return head

    def delete_at_position(self, head, pos):
        if head is None:
            return None
        idx = 0
        curr = head
        previous = None
        while curr.next and idx < pos:
            previous = curr
            curr = curr.next
            idx += 1

        if idx == 0:
            head = head.next
        else:
            previous.next = curr.next

        return head

    def insert_in_sorted_list(self, head, item):
        temp = Node(item)

        if head is None:
            return temp

        elif item < head.key:
            temp.next = head
            return temp
        else:
            curr = head

        while curr.next and curr.next.key < item:
            curr = curr.next

        temp.next = curr.next
        curr.next = temp
        return head

    def reverse_linked_list(self, head):
        curr = head
        prev = None

        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n

        return prev


if __name__ == "__main__":
    head = Node(10)
    head.next = Node(20)
    head.next.next = Node(30)
    head.next.next.next = Node(40)
    head.next.next.next.next = Node(50)
    head.next.next.next.next.next = Node(60)
    op = Operations()
    # op.print_list(head)
    # print()
    # print("size->",op.length_list(head))
    # print("position ->",op.search_in_list(head, 60))
    head = op.insert_start(head,5)
    head = op.insert_end(head, 70)
    head = op.insert_at_position(head, 35, 5)
    head = op.delete_first(head)
    head = op.delete_last(head)
    pos = 4
    idx = pos - 1
    head = op.delete_at_position(head,idx)
    head = op.insert_in_sorted_list(head, 35)
    # head = op.reverse_linked_list(head)
    op.print_list(head)
    print()