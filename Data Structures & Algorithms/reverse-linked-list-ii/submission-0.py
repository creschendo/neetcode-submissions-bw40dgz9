# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def getNext(node, k):
            while k > 0 and node:
                node = node.next
                k -= 1
            return node   
        dummy = ListNode(0, head)

        # retrieve the node before the one included in reverse
        prevNode = getNext(dummy, left - 1)

        # retrieve the last included node
        last = getNext(dummy, right)

        # store next excluded node
        nextNode = last.next
        
        # reverse the segment
        prev, curr = last.next, prevNode.next
        while curr != nextNode:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        # connect the left side
        prevNode.next = last

        return dummy.next


