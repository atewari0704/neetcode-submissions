class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        hashmap = dict()

        for src, dest, time in times:
           hashmap.setdefault(src, []).append([time, dest])
        
        if hashmap.get(k,-1) == -1:
            return -1
        
        
        pq = hashmap[k][::] # start from the source
        heapq.heapify(pq)
        visited,total = set(),0

        while pq and len(visited) < n - 1:
            cost,dest = heapq.heappop(pq)

            if dest in visited or dest == k:
                continue

            total = cost
            visited.add(dest)

            if hashmap.get(dest,None):
                for time, next_up in hashmap[dest]:
                    heapq.heappush( pq, [time + cost, next_up] )
            
        
        return total if (len(visited) == n - 1 and k not in visited) else -1