# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        sol = []
        def trav(node):
            if not node:
                return None
            sol.append(node.val)
            trav(node.left)
            trav(node.right)
        trav(root)
        return sol