class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        area = 0
        visited = set()

        def dfs(i,j):
            if (i < 0 or i >= ROWS 
                or j < 0 or j >= COLS
                or grid[i][j] == 0
                or (i,j) in visited):
                return 0 # not apart of adding to area

            #at a 1 which is not visited
            visited.add( (i,j) )

            return 1 + dfs(i+1,j) + dfs(i-1,j) + dfs(i,j+1) + dfs(i,j-1)
            


        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and  grid[i][j] == 1:
                    area = max(area,dfs(i,j))
        
        return area







        