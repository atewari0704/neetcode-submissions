class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = [grid[i][j] , 0]
                else:
                    grid[i][j] = [grid[i][j] , float("inf")]
    

        def dfs(i,j,time,visited): 
            if (i,j) in visited or i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) :
                 return # don't keep visiting the same things over and over


            visited.add( (i,j) )

            # time represents the time of tainting of this fruit
            # taint the adjacent fruit and the time of tainting is your own time + 1

            if grid[i][j][0] == 0:
                return

            if time < grid[i][j][1]:
                grid[i][j][1] = time


            directions = [(i - 1,j),(i + 1,j),(i,j - 1),(i,j + 1)]

            for di,dj in directions:
                dfs(di,dj,time + 1,visited)
            
            visited.remove( (i,j) )

        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == [2 , 0]:
                    dfs(i,j,0,set())

        mins = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == [1 , float("inf")]:
                    return -1

                mins = max(mins,grid[i][j][1])
        
        # print(grid)
        
        return mins

                

        

        