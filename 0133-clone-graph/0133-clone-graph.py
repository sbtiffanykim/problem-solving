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
        if not node:
            return None
        
        queue = deque([node])
        clone = {}
        clone[node] = Node(node.val)

        while queue:
            cur = queue.popleft()
            for neigbr in cur.neighbors:
                # If this neighbor has not been cloned yet, create its clone and add the neighbor to the queue
                if neigbr not in clone:
                    clone[neigbr] = Node(neigbr.val)
                    queue.append(neigbr)
                # Connect the cloned neighbor to the current node
                clone[cur].neighbors.append(clone[neigbr])
        
        return clone[node]