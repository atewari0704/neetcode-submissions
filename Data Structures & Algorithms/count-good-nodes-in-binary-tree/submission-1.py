# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#dfs where it is a good node where it is the max 

class Solution:
    def dfs(self, node, curMax):
        res = 0

        if not node:
            return 0

        if node.val >= curMax:
            curMax = max(node.val,curMax)
            res += 1
        
        res +=  self.dfs(node.left,curMax) + self.dfs(node.right,curMax)

        return res

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,root.val)


    

        