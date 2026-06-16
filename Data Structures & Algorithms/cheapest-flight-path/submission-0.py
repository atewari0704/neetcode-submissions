class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [float("inf")] * n
        costs[src] = 0

        for i in range(k+1):
            temp = costs.copy()

            for  start, stop, cost in flights:
                if costs[start] == float("inf"): continue

                if costs[start] + cost < temp[stop]:
                    temp[stop] = costs[start] + cost

            costs = temp
        
        if costs[dst] == float("inf"):
            return -1
        
        return costs[dst]

        return costs[dst] if not float("inf") else -1
