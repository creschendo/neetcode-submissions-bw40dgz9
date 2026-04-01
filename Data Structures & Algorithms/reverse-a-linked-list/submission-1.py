# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # set current and previous pointers
        curr = head
        prev = None

        # iterate through all nodes
        while curr != None:
            # save next node to temp variable
            temp = curr.next

            # set the new next to the previous node
            curr.next = prev

            # set the new prev to the current node
            prev = curr

            # move to the next node
            curr = temp
        
        # since we end on null, the first element will be
        # the last previous element
        return prev

