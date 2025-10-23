# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(root):
            if not root:
                return 0
            
            left = check_height(root.left)
            right = check_height(root.right)

            # If one side is unbalanced, or the current node is unbalanced
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            # Otherwise, return height
            return max(left, right) + 1
        
        return check_height(root) != -1