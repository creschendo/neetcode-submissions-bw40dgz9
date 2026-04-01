# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first, second = dummy, dummy

        # move pointers
        for _ in range(left - 1):
            first = first.next
        for _ in range(right):
            second = second.next

        # save nodes prior to rev group
        prevGroup = first
        first = first.next

        # save nodes after rev group
        nextGroup = second.next
        second.next = None

        # reverse portion
        prev = nextGroup
        while first:
            temp = first.next
            first.next = prev
            prev = first
            first = temp
        
        # reconnect on left side
        prevGroup.next = prev

        return dummy.next



         