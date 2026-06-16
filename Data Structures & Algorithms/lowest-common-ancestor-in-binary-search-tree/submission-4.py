# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        smaller = min(p.val,q.val)
        bigger = max(p.val,q.val)

        while root:
            if root.val < smaller: 
                root = root.right

            elif root.val > bigger: 
                root = root.left

            else: 
                return root



        