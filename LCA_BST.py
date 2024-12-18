"Time Complexity is O(H)"
"Space Complexity is O(H)"

#Explanation
"""If both p and q are smaller than root.val, search for the LCA in the left subtree.
Check Right Subtree: If both p and q are larger than root.val, search for the LCA in the right subtree.
Current Node is LCA: If p and q are on different sides or one matches root, root is the LCA.
Base Case: If root is None, return None to handle invalid inputs."""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return 

        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
        