# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevGroup = dummy
        while True:

            # Retrieve the next group's first pointer
            kth = self.getNext(prevGroup, k)
            if not kth:
                break
            nextGroup = kth.next

            # Reverse the current group
            prev, curr = kth.next, prevGroup.next
            while curr != nextGroup:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            # Connect the left side to the reverse portion
            temp = prevGroup.next
            prevGroup.next = kth
            prevGroup = temp

        return dummy.next

    # Returns the kth node in the group
    def getNext(self, node, k):
        while k > 0 and node:
            node = node.next
            k -= 1
        return node    
    