# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque([root])
        first_found = False
        first_set = set()
        parents_dict = {root:None}

        while queue:
            cur = queue.pop()

            if cur.val == p.val or cur.val == q.val:
                goes_up = cur                
                if not first_found:
                    first_found = True

                    while goes_up:
                        first_set.add(goes_up)
                        goes_up = parents_dict[goes_up]
                    
                else:
                    while goes_up:
                        if goes_up in first_set: 
                            return goes_up
                        goes_up = parents_dict[goes_up]
            
            
            if cur.left != None:
                parents_dict[cur.left] = cur
                queue.append(cur.left)

            if cur.right != None:
                parents_dict[cur.right] = cur
                queue.append(cur.right)
        
        return # this should never have to trigger
