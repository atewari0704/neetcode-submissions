# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val) # we have a new root

        cur_node = root

        while cur_node:
            if val > cur_node.val:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = TreeNode(val)
                    return root
            else:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = TreeNode(val)
                    return root

            