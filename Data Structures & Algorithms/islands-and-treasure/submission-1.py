class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS,COLS = len(grid),len(grid[0])

        q = deque([])
        visited = set()




        def helper(r,c):
            if (r < 0 or r >= ROWS or c < 0 or c >= COLS 
                or grid[r][c] == -1 or (r,c) in visited):
                return 
            
            q.append( (r,c) )
            visited.add( (r,c) )

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
        

        dist = 0 

        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist

                helper(r+1,c)
                helper(r-1,c)
                helper(r,c+1)
                helper(r,c-1)

            dist += 1


































        # def dfs(i,j,visited):
        #     if (i < 0 or i >= ROWS or j < 0 or j >= COLS 
        #         or grid[i][j] == -1 or (i,j) in visited):
        #         return 2147483647
            
        #     visited.add( (i,j) )
            
        #     if grid[i][j] not in [2147483647,-1]: return grid[i][j]

        #     return min(dfs(i+1,j,visited),
        #                     dfs(i-1,j,visited),
        #                     dfs(i,j+1,visited),
        #                     dfs(i,j-1,visited)) + 1

        # for i in range(ROWS):
        #     for j in range(COLS):
        #         if grid[i][j] == 2147483647:
        #             grid[i][j] = dfs(i,j,set())
            
        