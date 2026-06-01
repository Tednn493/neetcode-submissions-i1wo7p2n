# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        total = 0

        def dfs(root,prevMost):
            nonlocal total
            if not root:
                return
            if root.val>=prevMost:
                total+=1
                prevMost = max(prevMost,root.val)
            
            dfs(root.left,prevMost)
            dfs(root.right,prevMost)
        
        dfs(root,float('-inf'))
        return total
        

        