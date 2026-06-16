class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i:[] for i in range(n)}

        #populate the adj list with undirected edges
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        #perform dfs to see if there are cycles
        visited = set()

        # j is the current node and i is the parent we just came from
        # i is okay if already in visited because that's not indictive
        # of a cycle 
        def dfs(j,i):
            if j in visited: return False 

            visited.add(j)

            for child in adj[j]:
                # skip the parent 
                if child == i: continue

                if not dfs(child,j):
                    return False
            
            return True
        
        # we know for a fact that there will be a zeroith Node 
        
        return dfs(0,-1) and len(visited) == n




