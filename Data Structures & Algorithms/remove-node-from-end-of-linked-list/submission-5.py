# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        # create n + 1 distance between slow and fast, so slow
        # ends 1 before removed node
        for _ in range(n + 1):
            fast = fast.next
        
        # move slow to correct node
        while fast:
            fast = fast.next
            slow = slow.next

        # cut out removed node
        slow.next = slow.next.next

        return dummy.next
        
