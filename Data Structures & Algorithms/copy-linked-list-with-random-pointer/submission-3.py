"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        newList = ptr = Node(0)
        dummy = head

        # create copies
        while dummy:
            # create node copy and store in map
            copy = Node(dummy.val)
            copies[dummy] = copy

            # add to list contruct
            ptr.next = copy

            # move to next
            ptr = ptr.next
            dummy = dummy.next
        print(copies)
        # add random pointers
        ptr = newList.next
        dummy = head

        while dummy:
            if dummy.random:
                ptr.random = copies[dummy.random]
            else:
                ptr.random = None
            ptr = ptr.next
            dummy = dummy.next
        
        return newList.next

            
        

        