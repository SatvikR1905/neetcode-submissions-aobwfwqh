# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return None

            res.append(str(node.val))
            dfs(node.left) #pre-order BFS as it is easy as firt number in the list/array is root
            dfs(node.right)
        dfs(root)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split(",")
        i = [0]

        def dfs():
            if nodes[i[0]] == "N":
                i[0] += 1
                return None

            node = TreeNode(int(nodes[i[0]]))
            i[0] += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
