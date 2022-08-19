"""
203. Remove Linked List Elements

Given the head of a linked list and an integer val, remove all the nodes of the linked list
that has Node.val == val, and return the new head.

Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Input: head = [], val = 1
Output: []

Input: head = [7,7,7,7], val = 7
Output: []

Constraints:

    The number of nodes in the list is in the range [0, 104].
    1 <= Node.val <= 50
    0 <= val <= 50

"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if (head == None):
            return head

        dummyhead = ListNode(0)
        prev = dummyhead
        prev.next = head
        curr = head
        while (curr):
            if (curr.val == val):
                prev.next = curr.next
                rem = curr
                curr = curr.next
                del rem
            else:
                curr = curr.next
                prev = prev.next

        return dummyhead.next