# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ptr = head
        length = 0

        # find length of the list
        while ptr:
            length += 1
            ptr = ptr.next

        # take the second half and reverse it
        mid = length // 2
        rev = None
        ptr = head
        for _ in range(mid - 1):
            ptr = ptr.next

        temp = ptr.next
        ptr.next = None
        ptr = temp
        
        while ptr:
            temp = ptr
            ptr = ptr.next
            temp.next = rev
            rev = temp
        
        ptr = head
        
        while ptr.next and rev:
            temp1 = ptr.next
            temp2 = rev.next

            ptr.next = rev
            rev.next = temp1

            ptr = temp1
            rev = temp2
        
        ptr.next = rev



        
