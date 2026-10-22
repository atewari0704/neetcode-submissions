# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node,k):
            if not node: return None,k

            if node.left:
                res,k = dfs(node.left,k)
                if res: return res,k

        
            if k == 1:
                return node.val,k
            
            k -= 1 # till we get to the value we want

            if node.right:
                res,k = dfs(node.right,k)
                if res: return res,k
            
            return None,k
        

        return dfs(root,k)[0]
        