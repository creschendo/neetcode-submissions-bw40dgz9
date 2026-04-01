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


"""
    [1, 2, 3, 4, 5, 6]
    left = 2, right = 4

    dummy = ListNode(0, head)

    prevNode = getNext(dummy, left - 1)
    - prevNode = 1

    last = getNext(dummy, right)
    - last = 4

    nextNode = last.next
    - nextNode = 5

    prev, curr = last.next, prevNode.next
    - prev = 5, curr = 2

    while curr != nextNode:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    - [1, 2, 3, 4, 5, 6] -> [1 ... 4, 3, 2, 5, 6]

    prevNode.next = last
    - 1.next = 4
    - [1, 4, 3, 2, 5, 6]

    return dummy.next
"""
