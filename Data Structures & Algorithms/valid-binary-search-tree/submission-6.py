# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(root, window):
            if not root:
                return True
            elif root.val <= window[0]:
                return False
            elif root.val >= window[1]:
                return False
            else:
                return valid(root.left, [window[0], root.val]) and valid(root.right, [root.val, window[1]])
        
        return valid(root, [float('-inf'), float('inf')])