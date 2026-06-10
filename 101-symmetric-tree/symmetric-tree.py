# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetry(left,right):
            if root is None:
                return True
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return (left.val==right.val and symmetry(left.left,right.right) and symmetry(left.right,right.left))
        return symmetry(root.left,root.right)

        