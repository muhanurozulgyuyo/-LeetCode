# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # Initialize the sum variable
        total_sum = 0
        
        # Define a helper function for DFS
        def dfs(node):
            nonlocal total_sum
            
            if not node:
                return
            
            # If node's value is within the range, add it to the total_sum
            if low <= node.val <= high:
                total_sum += node.val
            
            # If node's value is greater than low, search in the left subtree
            if node.val > low:
                dfs(node.left)
            
            # If node's value is less than high, search in the right subtree
            if node.val < high:
                dfs(node.right)
        
        # Start the DFS from the root
        dfs(root)
        
        return total_sum
