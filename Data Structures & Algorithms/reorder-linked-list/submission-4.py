# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        # find the midpoint with slow and fast pointers
        # whenever the fast one reaches the end, the slow one reaches the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        half = slow.next
        slow.next = None

        # reverse the second half
        prev, curr = None, half
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        # splice the two lists together
        # since second is guaranteed to be shorter
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


