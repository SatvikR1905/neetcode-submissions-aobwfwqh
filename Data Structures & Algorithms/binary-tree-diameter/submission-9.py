# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        self.dfs(root, res)
        return res[0]
    
    def dfs(self, root, res):
            if root == None:
                return 0
            left = self.dfs(root.left,res)
            right = self.dfs(root.right,res)
            res[0] = max(res[0],left+right) # we r finding the largest length with the addition of a node compared to the result.
            return 1 + max(left,right)
                    