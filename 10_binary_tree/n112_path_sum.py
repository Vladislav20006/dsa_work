# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool: #O(n)
        if not root:
            return False #O(n)
        if not root.left and not root.right:
            return root.val == targetSum
        if self.hasPathSum(root.left, targetSum - root.val):
            return True #O(n)
        if self.hasPathSum(root.right, targetSum - root.val):
            return True #O(n)
        return False #O(h)