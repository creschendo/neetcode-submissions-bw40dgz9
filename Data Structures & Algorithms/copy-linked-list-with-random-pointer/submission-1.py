"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# Intuition:
# We can't directly create random mappings by the first iteration since the new list
# can't contain references to the old one.

# Thus, we must make copies on the first pass, skipping random mappings since the random
# pointer could point to a further node down the line whose copy hasn't been created yet

# Thus, we store the copies in a hashmap during the first pass, i.e. map[original] = copy
# On the second pass, we set the randoms by iterating through both lists, setting pointers to copies
# i.e. copy.random = copies[original.random]
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}
        # pointer to iterate original list
        ptr = head

        # new copy list
        dummy = curr = Node(0)
        while ptr:
            # create a copy of the current node
            newNode = Node(ptr.val)

            # add copy mapping
            copies[ptr] = newNode

            # add new node to copy list
            curr.next = newNode

            # move to next open copy slot
            curr = curr.next

            # move to next node in original lisst
            ptr = ptr.next

        # reset pointers
        curr = dummy.next
        ptr = head

        # add random pointers
        while ptr:
            if ptr.random != None:
                curr.random = copies[ptr.random]
            curr = curr.next
            ptr = ptr.next
        
        return dummy.next
