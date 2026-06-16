class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])

        visited,count = set(),0

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(r,c):
            if (r,c) in visited:
                return

            visited.add((r,c))

            for dr,dc in directions:
                nr,nc = r+dr,c+dc

                if nr >= ROWS or nr < 0 or nc >= COLS or nc < 0:
                    continue
                
                if grid[nr][nc] == "1":
                    dfs(nr,nc) 



        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visited or grid[r][c] == "0":
                    continue
                
                dfs(r,c)
                count += 1
        
        return count