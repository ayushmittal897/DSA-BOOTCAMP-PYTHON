# LC94: Binary Tree Inorder Traversal
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if node:
                dfs(node.left)
                res.append(node.val)
                dfs(node.right)
        dfs(root)
        return res
