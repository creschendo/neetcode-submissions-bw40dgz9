# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode()
        carry = 0
        while l1 and l2:
            # retrieve current values
            v1 = l1.val
            v2 = l2.val

            # find total sum
            total = v1 + v2 + carry

            # if it's greater than 10, add a carry
            # otherwise set carry to 0
            if total >= 10:
                carry = 1
            else:
                carry = 0

            # add tens digit to current node
            head.next = ListNode(total % 10)

            # move to next node
            head = head.next
            l1 = l1.next
            l2 = l2.next
        
        leftover = l1 if l1 else l2

        while leftover:
            # retrieve current values
            v1 = leftover.val
            v2 = carry

            # find total sum
            total = v1 + v2
            print("leftover total:" + str(total))
            # if it's greater than 10, add a carry
            # otherwise set carry to 0
            if total >= 10:
                print("carry 1")
                carry = 1
            else:
                print("carry 0")
                carry = 0

            # add tens digit to current node
            head.next = ListNode(total % 10)

            # move to next node
            head = head.next
            leftover = leftover.next
        
        if carry:
            head.next = ListNode(1)
        
        return dummy.next


