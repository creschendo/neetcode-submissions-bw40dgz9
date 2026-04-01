# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if not root:
                return []
            else:
                left = inorder(root.left)
                left.extend([root.val])
                left.extend(inorder(root.right))
                return left
        return inorder(root)