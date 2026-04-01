# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        queue.append(root)
        sol = []
        while queue:
            curr = []
            nodes = len(queue)
            for _ in range(nodes):
                node = queue.popleft()
                if node:
                    curr.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if curr:
                sol.append(curr)
        return sol



