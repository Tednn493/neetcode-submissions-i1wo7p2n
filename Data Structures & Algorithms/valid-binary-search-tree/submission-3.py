# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        l = float('-inf')
        r = float ('inf')

        return self.isValid(root,l,r)
    



    def isValid(self,root,l,r):
        if not root:
            return True
        if not (l < root.val < r):
            return False
        
        return self.isValid(root.left,l,root.val) and self.isValid(root.right,root.val,r)
            
    