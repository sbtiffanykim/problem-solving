# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if len(ans) <= depth:  # ensure ans has a sublist for this depth
                ans.append([])
            ans[depth].append(node.val)
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
        
        return ans