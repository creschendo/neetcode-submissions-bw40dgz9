"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Create a hashmap to hold copies
        copies = {}

        def helper(node):
            # if the node has already been copied, just return the copy
            if node in copies:
                return copies[node]

            # make a copy of the current node
            copy = Node(node.val)

            # add to the copies map
            copies[node] = copy

            # for each neighbor in original node, visit that node
            # and either make a copy or reuse an already made copy
            # and add to its neighbors field
            for neighbor in node.neighbors:
                copy.neighbors.append(helper(neighbor))
            
            # return the completed node copy
            return copy
        
        return helper(node) if node else None