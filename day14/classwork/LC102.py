from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
            
        q = deque([root])
        
        while q:
            level_size = len(q)
            level = []
            for _ in range(level_size):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
            
        return res

"""
Approach:
Breadth-First Search (BFS) using a Queue.
We push the root to the queue. In each step, we process all nodes currently in the queue (which represents one level),
and push their children to the back of the queue for the next level.
"""
