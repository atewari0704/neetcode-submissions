class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adj = defaultdict(list)
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        

        # cur_visit = set()

        def dfs(node, parent):
            # if node in cur_visit:
            #     return 0 
            
            # cur_visit.add(node)
            cost = 0

            for child in adj[node]:
                if child == parent:
                    continue 

                cost += dfs(child, node)
            
            if (cost > 0 or hasApple[node]) and node != 0:
                cost += 2
            
            # cur_visit.remove(node)
            return cost


        return dfs(0, None)
        