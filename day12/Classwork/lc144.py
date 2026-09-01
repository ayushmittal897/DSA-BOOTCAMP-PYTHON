# lc144.py
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node):
            if node is None:
                return

            ans.append(node.val)   # Root
            dfs(node.left)         # Left
            dfs(node.right)        # Right

        dfs(root)
        return ans
