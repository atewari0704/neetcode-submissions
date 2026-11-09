class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        pq = []

        res = 0
        max_possible_i = len(heights) - 1

        heapq.heappush(pq, (0,bricks,ladders))

        while pq:
            cur_i, cur_bricks, cur_ladders = heapq.heappop(pq)
            res = max(res,cur_i)

            if cur_i == max_possible_i:
                return cur_i
            
            if heights[cur_i + 1] > heights[cur_i]:
                diff = heights[cur_i + 1] - heights[cur_i]

                if cur_bricks >= diff:
                    heapq.heappush(pq, (cur_i + 1,cur_bricks - diff,cur_ladders))
                
                if ladders:
                    heapq.heappush(pq, (cur_i + 1,cur_bricks,cur_ladders - 1))
            
            else:
                heapq.heappush(pq, (cur_i + 1,cur_bricks,cur_ladders))

        return res


