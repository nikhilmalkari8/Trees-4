# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = []
        pathA = []
        pathB = []
        def helper(node):
            path.append(node)
            
            if node == p:
                pathA.extend(path.copy())
            if node == q:
                pathB.extend(path.copy())
            
            if node.left:
                helper(node.left)
            
            if node.right:
                helper(node.right)
            
            path.pop()
        
        helper(root)
        
        lca = None
        for i,j in zip(pathA, pathB):
            if i == j:
                lca = i
            else:
                break
        
        return lca