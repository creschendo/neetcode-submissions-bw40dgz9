# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        diff = float('-inf')
        def helper(root):
            nonlocal diff
            if not root:
                return 0
            left = helper(root.left)
            right = helper(root.right)
            diff = max(diff, abs(left - right))
            return 1 + max(left, right)
        helper(root)
        print(diff)
        return diff <= 1
