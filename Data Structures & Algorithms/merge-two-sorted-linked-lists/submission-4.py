# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = list1, list2
        dummy = head = ListNode(0)

        while p1 and p2:
            if p1.val < p2.val:
                head.next = ListNode(p1.val)
                head = head.next
                p1 = p1.next
            else:
                head.next = ListNode(p2.val)
                head=head.next
                p2 = p2.next
            

        if p1:
            head.next = p1
        elif p2:
            head.next = p2
        
        return dummy.next
