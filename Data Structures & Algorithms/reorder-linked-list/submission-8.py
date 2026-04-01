# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # find midpoint to split
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split list
        secondHalf = slow.next
        slow.next = None

        # reverse second half
        prev, curr = None, secondHalf
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first = head
        second = prev

        # splice lists together
        while second:
            firstNext = first.next
            secondNext = second.next
            first.next = second
            second.next = firstNext
            first = firstNext
            second = secondNext
            

    