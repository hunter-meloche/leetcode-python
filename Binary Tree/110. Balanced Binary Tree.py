# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            # If root is None then give a True boolean and a 0 depth back
            if root is None: 
                return [True, 0]

            # Recursively determine if there are children nodes and their respective depths
            left = dfs(root.left)
            right = dfs(root.right)

            # Determine the tree is balanced if left and right children are not unbalanced themselves 
            # and do not have greater than one level of depth difference
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

            # Return whether or not the tree is balanced and its depth
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]
