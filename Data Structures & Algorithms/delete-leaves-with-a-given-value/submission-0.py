# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def helper(root, val):
            if not root:
                return None
            else:
                root.left = helper(root.left, val)
                root.right = helper(root.right, val)

                if not root.left and not root.right and root.val == val:
                    return None
                else:
                    return root


        return helper(root, target)