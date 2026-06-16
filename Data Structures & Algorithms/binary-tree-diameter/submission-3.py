# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def max_diameter(node):
            left_len,right_len = 0,0

            if node.left: 
                left_len =  max_diameter(node.left) + 1;
            

            if node.right: 
                right_len =  max_diameter(node.right) + 1;
            
            self.diameter = max(self.diameter,left_len+right_len)

            return max(left_len,right_len)
        
        max_diameter(root)
    
        return self.diameter

        