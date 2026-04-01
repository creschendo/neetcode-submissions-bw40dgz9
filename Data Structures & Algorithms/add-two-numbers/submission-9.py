# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        carry = 0
        while l1 or l2 or carry:
            # retrieve current values
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            # find total sum
            total = v1 + v2 + carry

            # if it's greater than 10, add a carry
            # otherwise set carry to 0
            carry = total // 10

            # add tens digit to current node
            head.next = ListNode(total % 10)

            # move to next node
            head = head.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next


