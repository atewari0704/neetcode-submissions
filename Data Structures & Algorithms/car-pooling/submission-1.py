class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pq = []
        for cost,start,end in trips:
            pq.append( [start, 1,  -1 * cost] )
            pq.append( [end, -1,  cost] )

        print(pq)
        
        heapq.heapify(pq)

        cur_cap = capacity
        while pq:
            point,type_of,cost = heapq.heappop(pq)

            cur_cap += cost

            if cur_cap < 0 : return False
        
        return True


        