# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def __init__(self):
    #     self.diameter = 0 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_height_dict = {}
        stack = [(root,False)]
        diameter = 0

        while stack:
            node,visited = stack.pop()

            if not visited:
                stack.append((node,True))

                if node.left: stack.append((node.left,False))

                if node.right: stack.append((node.right,False))

            else:
                if not node.left:
                    left_height = 0
                else:
                    left_height = max_height_dict[node.left] 
                
                if not node.right:
                    right_height = 0
                else:
                    right_height = max_height_dict[node.right]

                diameter = max(diameter,left_height + right_height)

                max_height_dict[node] = max(left_height,right_height) + 1
        
        return diameter









        # def max_diameter(node):
        #     left_len,right_len = 0,0

        #     if node.left: 
        #         left_len =  max_diameter(node.left) + 1;
            

        #     if node.right: 
        #         right_len =  max_diameter(node.right) + 1;
            
        #     self.diameter = max(self.diameter,left_len+right_len)

        #     return max(left_len,right_len)
        
        # max_diameter(root)
    
        # return self.diameter

        