class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)

        for start,end,cost in flights:
            adj[start].append([cost,end])
        
        q = [ [0,src,0] ] #cost,dest,stops

        heapq.heapify(q)

        while q:
            cost, dest, stops = heapq.heappop(q)

            if stops > k and dest != dst:
                continue 
            
            if dest == dst:
                return cost 
            
            for add_cost,nei in adj[dest]:
                new_cost = add_cost + cost
                heapq.heappush(q,[new_cost, nei, stops+1])

        return -1


        
        



    