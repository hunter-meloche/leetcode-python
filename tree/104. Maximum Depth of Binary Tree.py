# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        depth = 1
        left = 0
        right = 0
        if root.left is not None:
            left = self.maxDepth(root.left)
        if root.right is not None:
            right = self.maxDepth(root.right)
        if left - right > 0:
            depth += left
        else:
            depth += right
        return depth
