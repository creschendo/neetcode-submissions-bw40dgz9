"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def helper(grid):
            # create new node
            newNode = Node()

            # check if all values in grid are the same
            same = len({cell for row in grid for cell in row}) == 1

            if same:
                newNode.val = grid[0][0]
                newNode.isLeaf = True
                newNode.topLeft = None
                newNode.topRight = None
                newNode.bottomLeft = None
                newNode.bottomRight = None
                return newNode

            else:
                mid = len(grid) // 2
                topLeft = [row[:mid] for row in grid[:mid]]
                topRight = [row[mid:] for row in grid[:mid]]
                botLeft = [row[:mid] for row in grid[mid:]]
                botRight = [row[mid:] for row in grid[mid:]]

                newNode.val = 0
                newNode.isLeaf = False
                newNode.topLeft = helper(topLeft)
                newNode.topRight = helper(topRight)
                newNode.bottomLeft = helper(botLeft)
                newNode.bottomRight = helper(botRight)

            return newNode
            
        return helper(grid)

