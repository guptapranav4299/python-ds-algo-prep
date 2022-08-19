"""
25. Reverse Nodes in k-Group

Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the number
of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]



Constraints:

    The number of nodes in the list is n.
    1 <= k <= n <= 5000
    0 <= Node.val <= 1000


"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def length(self, head):
        len = 0
        curr = head
        while curr is not None:
            len += 1
            curr = curr.next
        return len

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or k == 1:
            return head
        curr = head
        fwd = None
        prev = None

        mover = 0
        while mover < k and curr is not None:
            fwd = curr.next
            curr.next = prev
            prev = curr
            curr = fwd
            mover += 1
        if fwd is not None and self.length(fwd) >= k:
            head.next = self.reverseKGroup(fwd, k)
        else:
            head.next = curr
            return prev
        return prev
