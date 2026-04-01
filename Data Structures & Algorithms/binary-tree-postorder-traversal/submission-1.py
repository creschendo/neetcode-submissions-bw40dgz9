# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.sol = []

        def trav(root):
            if not root:
                return 
            trav(root.left)
            trav(root.right)
            self.sol.append(root.val)
        trav(root)
        return self.sol
