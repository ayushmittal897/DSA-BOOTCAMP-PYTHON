# LC113: Path Sum II
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, curr_sum, path):
            if not node:
                return
            curr_sum += node.val
            path.append(node.val)
            if not node.left and not node.right and curr_sum == targetSum:
                res.append(list(path))
            else:
                dfs(node.left, curr_sum, path)
                dfs(node.right, curr_sum, path)
            path.pop()
        dfs(root, 0, [])
        return res
