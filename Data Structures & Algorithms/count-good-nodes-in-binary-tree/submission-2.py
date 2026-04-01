# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def helper(root, val):
            if not root:
                return 0
            return (root.val >= val) + helper(root.left, max(root.val, val)) + helper(root.right, max(root.val, val))

        return helper(root, float('-inf'))