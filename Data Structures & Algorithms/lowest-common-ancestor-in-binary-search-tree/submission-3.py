# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # could just do return root at the end, but show all cases
        
        # if the current root lies between the two subnodes
        # they must have diverged here
        if p.val < root.val < q.val or q.val < root.val < p.val:
            return root
        
        # if the root is equal to either node, its the LCA
        elif root.val == p.val or root.val == q.val:
            return root

        # if both values are less than root, check left
        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        
        # if both values are greater than root, check right
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)