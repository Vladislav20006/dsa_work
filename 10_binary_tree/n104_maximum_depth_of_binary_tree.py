# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: #O(n)
        if not root:
            return 0 #O(n)
        else:
            l_depth = self.maxDepth(root.left)
            r_depth = self.maxDepth(root.right)
            return max(l_depth, r_depth) + 1 #O(n)