# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        sol = []
        while queue:
            elems = len(queue)
            for i in range(elems):
                item = queue.popleft()
                if item.right:
                    queue.append(item.right)
                if item.left:
                    queue.append(item.left)
                if i == 0:
                    sol.append(item.val)
                

        return sol