# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        sol = root.val
        def helper(node):
            nonlocal sol
            if not node:
                return 0
            left = max(helper(node.left), 0)
            right = max(helper(node.right), 0)

            sol = max(sol, node.val + left + right)

            return node.val + max(left, right)
        helper(root)
        return sol