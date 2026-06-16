class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for n in range(n)] # neighbors
        vis = [False] * n  # intially not visited any neighbors

        def dfs(n):
            for nei in adj[n]:
                if not vis[nei]:
                    vis[nei] = True
                    dfs(nei)


        components = 0 

        # populate neighbors
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for n in range(n):
            if not vis[n]:
                vis[n] = True # now we have visited it 
                dfs(n) 
                components += 1
        
        return components


        