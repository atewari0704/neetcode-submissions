"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root


        q = deque([root])

        while q:
            level_len = len(q)
            # for i in range(level_len):
            #     cur = q[i]

            #     if i+1 < level_len:
            #         cur.next = q[i+1]

            for i in range(level_len):
                if i+1 < level_len:
                    q[0].next = q[1]

                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)
                
                if cur.right:
                    q.append(cur.right)

        return root

        