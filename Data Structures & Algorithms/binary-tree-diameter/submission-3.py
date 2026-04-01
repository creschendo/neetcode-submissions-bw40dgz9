# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        sol = 0

        def trav(root):
            nonlocal sol
            if not root:
                return 0
            
            left, right = trav(root.left), trav(root.right)

            sol = max(sol, left + right)
            return max(left, right) + 1
        trav(root)
        return sol