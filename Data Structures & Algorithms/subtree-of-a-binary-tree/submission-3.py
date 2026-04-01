# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return False
            return equal(root, subRoot) or helper(root.left) or helper(root.right)

        def equal(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and equal(p.left, q.left) and equal(p.right, q.right)
        return helper(root)