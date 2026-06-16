class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        

        def dfs(node, parent):
            cost = 0

            for child in adj[node]:
                if child == parent:
                    continue 

                cost += dfs(child, node)
            
            if (cost > 0 or hasApple[node]) and node != 0:
                cost += 2
            
            return cost


        return dfs(0, None)
        