# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def helper(root, subRoot):
            if root == None:
                return False
            if root.val == subRoot.val:
                if isSameTree(root, subRoot):
                    return True
            return helper(root.left, subRoot) or helper(root.right, subRoot)
            
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            # if both none, fine
            if not p and not q:
                return True
            
            # if one not none, not fine
            elif p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            
            return False
        return helper(root, subRoot)