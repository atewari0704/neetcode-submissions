class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)}

        #calculating the costs from a point to all the other points
        for i in range(N):
            x1,y1 = points[i]
            for j in range(i+1,N):
                x2,y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)

                adj[i].append([cost,j])
                adj[j].append([cost,i])
        
        
        total = 0
        visited = set()
        visited.add(0)
        pq = adj[0][::]
        heapq.heapify(pq)

        while len(visited) < N:
            cost, i = heapq.heappop(pq)

            if i in visited:
                continue
            
            total += cost
            visited.add(i)

            for arr in adj[i]:
                heapq.heappush(pq,arr)
        
        return total




