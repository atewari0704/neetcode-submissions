# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_arr, q_arr = [], []

        def get_chain(node,target,arr):
            if node == target:
                arr.append(node)
                return True
            
            if node.left:
                if get_chain(node.left,target,arr):
                    arr.append(node)
                    return True
            
            if node.right:
                if get_chain(node.right,target,arr):
                    arr.append(node)
                    return True
        
        get_chain(root,p,p_arr)
        get_chain(root,q,q_arr)

        p_set = set(p_arr)

        for ancestor in q_arr:
            if ancestor in p_set: 
                return ancestor
