# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Learning DFS. 
        We know 1 is starting depth if we have a root node, traverse the left side
        and right side. Add that to the max and return that.
        TC: O(N) Going through all nodes
        SC: O(N) best case O(log(N)) if balanced else O(N)
        '''
        if not root:
            return 0
        return 1+ max(self.maxDepth(root.left),self.maxDepth(root.right))