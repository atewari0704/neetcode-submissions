class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = collections.defaultdict(list)

        #create a dict where we map conversions
        for i, equation in enumerate(equations):
            src,dest = equation
            adj[src].append( (dest, values[i]) )
            adj[dest].append( (src, 1/values[i]) )
        
        def bfs(src,dest):
            if src == dest and src in adj and dest in adj: return 1
            if src not in adj or dest not in adj:
                return -1
            
            q,visit = deque([(src, 1)]), set()

            while q:
                cur_n,cur_w = q.popleft()
                visit.add(cur_n)

                for n,w in adj[cur_n]:
                    if n in visit: continue

                    if n == dest:return cur_w * w

                    q.append((n,cur_w * w))

            return -1 
        

        return [bfs(src,dest) for src,dest in queries]


