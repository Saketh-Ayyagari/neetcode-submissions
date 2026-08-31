# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    """
    Checks if two trees are the same given their roots
    """
    def isSameTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # base case
        if not root1 and not root2:
            return True
        elif root1 and root2 and root1.val == root2.val:
            return True and self.isSameTree(root1.left, root2.left) and self.isSameTree(root1.right, root2.right)
        else:
            return False
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # base case: subRoot is empty -> return True
        if not subRoot:
            return True
        if not root:
            return False
        # base case: root1 == root2 -> check if they're the same tree
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        