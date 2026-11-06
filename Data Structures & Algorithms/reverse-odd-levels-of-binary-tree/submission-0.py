# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        odd = False #represents if we are on an odd or even level

        queue = deque([root])

        while queue:
            if odd:
                length = len(queue) 
                for i in range(length//2):
                    a = queue[i]
                    b = queue[length - 1 - i]

                    temp = a.val
                    a.val = b.val
                    b.val = temp
                
                for i in range(len(queue)):
                    node = queue.popleft()

                    if node.left and node.right:
                        queue.append(node.left)
                        queue.append(node.right)
                
                odd = False
                
            else:
                for i in range(len(queue)):
                    node = queue.popleft()

                    if node.left and node.right:
                        queue.append(node.left)
                        queue.append(node.right)
                    
                odd = True
                
        return root
                    


        