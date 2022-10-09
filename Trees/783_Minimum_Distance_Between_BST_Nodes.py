# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Needed help.
    Since it is a BST, we can use In Order traversal to get the nodes in order.
    Make global variables to keep in track of the minDiff.
    TC: O(N) we have to traverse the whole tree
    SC: O(H) where H is the height of tree, 
    This is the space used by the implicit call stack when calling dfs.
    '''
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.minDiff = float("inf")
        self.previous = float("inf")
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            
            #Juicy part of in-order traversal
            #Takes the min of ABS of whatever previous and current root val
            #ABS because difference is the only thing that matters, not posi/nega.
            self.minDiff = min(self.minDiff, abs(self.previous-root.val))
            self.previous = root.val
            
            dfs(root.right)
        
        dfs(root)
        
        return self.minDiff
        