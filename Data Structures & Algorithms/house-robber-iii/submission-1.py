class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node):          
            if not node:
                return (0, 0)

            left = dfs(node.left)
            right = dfs(node.right)

            rob = node.val + left[1] + right[1]
            skip = max(left[0], left[1]) + max(right[0], right[1])

            return (rob, skip)
        
        result = dfs(root)      
        return max(result[0], result[1])