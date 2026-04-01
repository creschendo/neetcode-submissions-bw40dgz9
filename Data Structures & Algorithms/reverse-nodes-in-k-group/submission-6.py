# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # returns the kth node in the group
        def kth(node, k):
            while node.next:
                node = node.next
                k -= 1
                if not k:
                    return node
            return None

        dummy = curr = ListNode(0, head)

        while curr.next:
            # grab kth node
            last = kth(curr, k)

            # if less than k, break
            if not last:
                break
            
            # grab next group
            nextGroup = last.next

            # sever right side
            last.next = None

            # get previous group
            prevGroup = curr
            
            # move to first rev
            curr = curr.next

            # save first, since it will be start of next
            save = curr

            # reverse current group
            prev = nextGroup
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # set new curr to prior first, since it's last now
            curr = prevGroup.next

            # reconnect left side
            prevGroup.next = prev
        
        return dummy.next