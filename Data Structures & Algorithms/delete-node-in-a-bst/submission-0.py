# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if not root.left: #case 1 and 2
                return root.right
            elif not root.right:
                return root.left
            
            #case 3 when you have two children
            minval = root.right # we go right because we cant put values present in the left sub tree as they are already small and can diturb the BST architecture
            while minval.left:
                minval = minval.left
            root.val = minval.val # we assign the smallest value we got to the current node
            root.right = self.deleteNode(root.right, minval.val) # we delete the duplicate record
        return root
            
        