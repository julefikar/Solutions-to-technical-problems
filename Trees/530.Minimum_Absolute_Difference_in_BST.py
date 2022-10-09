# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.minDiff = float("inf")
        self.previous = float("inf")
        
        def dfs(root):
            if not root: return 
            dfs(root.left)
            self.minDiff = min(self.minDiff, abs(self.previous-root.val))
            self.previous = root.val
            dfs(root.right)
        
        dfs(root)
        
        return self.minDiff