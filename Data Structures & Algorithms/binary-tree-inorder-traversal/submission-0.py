# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        def trav(node):
            if not node:
                return None
            left = trav(node.left)
            if left:
                sol.append(left)
            sol.append(node.val)
            right = trav(node.right)
            if right:
                sol.append(right)
        trav(root)
        return sol
        