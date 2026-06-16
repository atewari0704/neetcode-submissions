# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []

        res,queue = [],deque([root])

        while queue:
            cur_level = len(queue)

            for i in range(cur_level):
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)

                if cur.right:
                    queue.append(cur.right)

                
            res.append(cur.val)
        
        return res





