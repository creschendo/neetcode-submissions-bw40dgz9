# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        sol = []

        def helper(node):
            if not node:
                return
            helper(node.left)
            sol.append(node.val)
            helper(node.right)
        
        helper(root)
        return sol[k-1]