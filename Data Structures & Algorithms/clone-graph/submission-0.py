"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = dict()

        def dfs(root):
            if root == None: return

            print(root.val)
            print("visited: ",visited)

            root_copy = Node(root.val)

            visited[root_copy.val] = root_copy # the node itself is mutable so it should update

            neighbors_copy = [] # copy of ALL the neighbors

            for neighbor in root.neighbors:
                if neighbor.val in visited:
                    neighbor_copy = visited[neighbor.val]
                else:
                    neighbor_copy = dfs(neighbor)
                
                neighbors_copy.append(neighbor_copy)

            root_copy.neighbors = neighbors_copy
            
            return root_copy
        
        return dfs(node)


