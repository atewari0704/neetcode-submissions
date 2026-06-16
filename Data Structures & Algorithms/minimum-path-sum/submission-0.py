class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS,COLS = len(grid),len(grid[0])
        for i in range(ROWS):
            for j in range(COLS):
                top,left = None,None

                #check top
                if i - 1 >= 0: top = grid[i-1][j]

                #check left
                if j - 1 >= 0: left = grid[i][j - 1]

                if top and left:
                    grid[i][j] += min(top,left) 

                elif top:
                    grid[i][j] += top

                elif left:
                    grid[i][j] += left
        
        return grid[ROWS-1][COLS-1]





        