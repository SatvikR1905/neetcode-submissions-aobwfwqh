# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #if two trees doesnt exisist still its same
            return True
        if not p or not q: #if either one of the tree is missing
            return False
        if p.val != q.val: #if rrot node values are missing
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) #recursive call to check if two subtrees match
        