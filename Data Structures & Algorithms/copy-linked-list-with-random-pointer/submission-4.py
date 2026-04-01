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
        dummy = node = head
        newList = copynode = Node(0, None)

        # first pass
        # make initial copies and store copies in hashmap for later random assignment
        while node:
            # create copy
            newNode = Node(node.val)

            # link copy list to new node
            copynode.next = newNode

            # map existing node to copy
            copies[node] = newNode

            # move both pointers
            node = node.next
            copynode = copynode.next

        # second pass
        node = dummy
        copynode = newList.next

        while node:
            # set random
            random = node.random
            if random in copies:
                copynode.random = copies[random]
            else:
                copynode.random = None

            # move pointers
            node = node.next
            copynode = copynode.next
        
        return newList.next
