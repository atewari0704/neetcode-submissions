# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        #bottom up approach

        def dfs(root):
            if not root: return[0,0] # with root, without root

            left_pair = dfs(root.left)
            right_pair = dfs(root.right)

            #with root
            with_root = root.val + left_pair[1] + right_pair[-1]

            without_root = max(left_pair) + max(right_pair)

            return [with_root,without_root]



        return max(dfs(root))


        # def check_all(cur, eligible):
        #     if not cur:
        #         return 0
            
        #     if eligible == 0:
        #         left_include = check_all(cur.left,1)
        #         right_include = check_all(cur.right,1)

        #         return left_include + right_include
            
        #     else:
        #         # given a node is elgible they may choose to not join

        #         #chosing not to join so therefore the children are eligible
        #         left_include = check_all(cur.left,1)
        #         right_include = check_all(cur.right,1)

        #         exclude_cur = left_include + right_include


        #         left_exclude = check_all(cur.left,0)
        #         right_exclude = check_all(cur.right,0)

        #         include_cur = cur.val + left_exclude + right_exclude

        #         return max(exclude_cur,include_cur)
        
        # return check_all(root,1)

