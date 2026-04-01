# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def helper(p, q):
            # if both none, fine
            if not p and not q:
                return True
            
            # if one not none, not fine
            elif p and q and p.val == q.val:
                return helper(p.left, q.left) and helper(p.right, q.right)
            
            return False
        return helper(p, q)