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
        # node creator, creates empty placeholders on first key access
        # algo initally sets references, then fills out values as loop goes on
        oldToCopy = collections.defaultdict(lambda: Node(0))

        # allows for None accesses
        oldToCopy[None] = None

        cur = head
        while cur:

            # sets value, possibly creates new node
            oldToCopy[cur].val = cur.val

            # sets references to next node
            oldToCopy[cur].next = oldToCopy[cur.next]

            # sets reference to random node
            oldToCopy[cur].random = oldToCopy[cur.random]

            # increment
            cur = cur.next
        return oldToCopy[head]