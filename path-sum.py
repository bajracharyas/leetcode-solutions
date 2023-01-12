# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def hasPathTarget(root, target):
            #print(root.val, target)
            if root == None:
                return False
            if root.left == None and root.right == None:
                return root.val == target
            return hasPathTarget(root.left, target - root.val) or hasPathTarget(root.right, target - root.val)
        
        return hasPathTarget(root, targetSum)