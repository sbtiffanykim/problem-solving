"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}

        def dfs(node):
            if node in clone:
                return clone[node]
            
            # Clone the current node
            cur = Node(node.val)
            clone[node] = cur

            for neigbr in node.neighbors:
                cur.neighbors.append(dfs(neigbr))
            
            return cur
        
        return dfs(node) if node else None