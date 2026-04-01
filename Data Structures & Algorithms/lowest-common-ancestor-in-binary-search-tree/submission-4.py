# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def helper(root, p, q):
            if not root:
                return None
            if root.val == p.val or root.val == q.val:
                return root
            if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
                return root
            if root.val > p.val and root.val > q.val:
                return helper(root.left, p, q)
            if root.val < p.val and root.val < q.val:
                return helper(root.right, p, q)
        return helper(root, p, q)