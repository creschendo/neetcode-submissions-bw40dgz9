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
            children = deque()
            while queue:
                node = queue.popleft()
                if not node:
                    continue
                curr.append(node.val)
                children.append(node.left)
                children.append(node.right)
            if curr:
                sol.append(curr)
            queue = children
        return sol



