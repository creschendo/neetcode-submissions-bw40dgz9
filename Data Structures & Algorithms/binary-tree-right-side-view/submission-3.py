# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        # Add first queue node into solution, add all children 
        # from right to left
        queue = deque([root])
        sol = []
        while queue:
            # size of the current level
            size = len(queue)
            for i in range(size):
                # pop the node
                node = queue.popleft()

                # if first node in queue, add to solution
                if i == 0:
                    sol.append(node.val)

                # add right children
                if node.right:
                    queue.append(node.right)
                
                # add left children
                if node.left:
                    queue.append(node.left)
        
        return sol