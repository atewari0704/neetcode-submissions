# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        NoneFound = False

        q = deque([root])


        while q:
            cur = q.popleft()

            if cur == None:
                NoneFound = True
                # for item in q:
                #     if item: return False
                # return True

            
            else:
                if NoneFound:
                    return False
                    
                q.append(cur.left)
                q.append(cur.right)
        
        return True


