# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        '''
        Use recursion, make right and left subtree recurse until all vals are copied, then set the childrens values to them.
        TC: O(N)
        SC: O(N)
        '''
        if not root:
            return None
        rightTree = self.invertTree(root.right)
        leftTree = self.invertTree(root.left)
        root.right = leftTree
        root.left = rightTree
        return root