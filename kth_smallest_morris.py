"Time Complexity is O(N)"
"Space Complexity is O(1)"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        count = 0

        while current:
            if current.left is None:
                count += 1
                if count == k:
                    return current.val
                current = current.right
            else:
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = current
                    current = current.left
                else:
                    predecessor.right = None
                    count += 1
                    if count == k:
                        return current.val
                    current = current.right
