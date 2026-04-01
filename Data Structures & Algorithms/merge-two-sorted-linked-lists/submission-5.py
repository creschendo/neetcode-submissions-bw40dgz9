# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        head = dummy
        p1, p2 = list1, list2

        while p1 and p2:
            if p1.val <= p2.val:
                head.next = p1
                head = head.next
                p1 = p1.next
            else:
                head.next = p2
                head = head.next
                p2 = p2.next
        
        head.next = p1 if p1 else p2

        return dummy.next
