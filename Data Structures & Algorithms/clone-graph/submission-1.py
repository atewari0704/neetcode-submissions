"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return

        root_copy = Node(node.val)
        visited = {root_copy.val: root_copy}

        queue = deque([node])

        while queue:
            cur = queue.popleft()

            cur_copy = visited[cur.val] # this is the Node copy itself

            for neighbor in cur.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor) #appending the OG neighbor

                cur_copy.neighbors.append(visited[neighbor.val])

        return root_copy
