# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_queue,q_queue = deque([p]),deque([q])

        while p_queue and q_queue:
            p_node,q_node = p_queue.popleft(),q_queue.popleft()

            if p_node == None and q_node == None: continue

            elif (p_node and q_node) and (p_node.val == q_node.val): 
                p_queue.append(p_node.left); p_queue.append(p_node.right);

                q_queue.append(q_node.left); q_queue.append(q_node.right);
            
            else:
                return False

        return True
        