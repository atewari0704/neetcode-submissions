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
        level = 0 

        while queue:
            if level%2 != 0:
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
                
            level += 1

        return root
                    


        