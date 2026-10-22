# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            nonlocal k

            if not node: return None

            if node.left:
                res = dfs(node.left)
                if res != None: return res

        
            if k == 1:
                print(node.val)
                return node.val
            
            k -= 1 # till we get to the value we want

            if node.right:
                res = dfs(node.right)
                if res != None: return res
            
            return None
        

        return dfs(root)
        