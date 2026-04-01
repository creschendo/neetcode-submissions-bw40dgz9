# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # create queue to use bfs
        queue = deque([root])
        sol = []


        while queue:
            # current level of tree
            curr = []

            # number of nodes to add
            nodes = len(queue)

            # for each node, add the value to the current 
            # and add children to queue
            for _ in range(nodes):
                node = queue.popleft()
                if node:
                    curr.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            
            # add complete level
            if curr:
                sol.append(curr)

        return sol



