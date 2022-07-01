# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def checkTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        '''
        Just return T/F if val of root is equal to left child + right child.
        TC: O(1)
        SC: O(1)
        '''
        return root.val == (root.left.val + root.right.val)
        