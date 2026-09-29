# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # base case: if we reach the end of a path, then check if the pathsum == targetSum
        # to do this, if we subtract all values from a targetSum, we should end up with 0

        # another base case: if node is null, tree is empty, so return false
        if (root == None):
            return False
        # otherwise, call hasPathSum() on left and right children ONLY IF those children exist
        # note we have to subtract the value of the current node (acts as a "counting")
        if (root.left and root.right): # both children exist
            return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)
        elif (root.left): # only left exists
            return self.hasPathSum(root.left, targetSum - root.val)
        elif (root.right): # only right exists
            return self.hasPathSum(root.right, targetSum - root.val)
        else: # no children exist, so this handles our base case
            # subtract current value from targetSum
            check = targetSum - root.val
            return (check == 0)