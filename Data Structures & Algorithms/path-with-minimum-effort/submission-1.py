class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS,COLS = len(heights),len(heights[0])
        min_heap = [[0,0,0]] # diff,row,cols
        visited = set()
        directions = [[1,0],[-1,0],[0,-1],[0,1]]


        while min_heap:
            diff, r ,c = heapq.heappop(min_heap)

            if (r,c) in visited:
                continue
            
            visited.add( (r,c) ) 

            if r == ROWS - 1 and c == COLS - 1:
                return diff

            
            for dr,dc in directions:
                if r + dr < 0 or c + dc < 0 or r + dr >= ROWS or c + dc >= COLS or (r+dr,c+dc) in visited:
                    continue
                
                cur_diff = abs(heights[r+dr][c+dc] - heights[r][c])
                
                heapq.heappush(min_heap,[max(diff,cur_diff), r+dr, c + dc])
            



       