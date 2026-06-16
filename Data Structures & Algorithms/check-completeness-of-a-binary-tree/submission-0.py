# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        q = deque([root])


        while q:
            cur = q.popleft()

            if cur == None:
                for item in q:
                    if item: return False
            
            else:
                q.append(cur.left)
                q.append(cur.right)
        
        return True


