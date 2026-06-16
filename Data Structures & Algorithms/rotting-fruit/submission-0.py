class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh,time = 0,0
        queue = deque() #rotten fruits

        ROWS,COLS = len(grid), len(grid[0])

        #Keeping track of the fresh and rotten fruits 
        for r in range(ROWS):
            for c in range(COLS):
                cur = grid[r][c]
                if cur == 1:
                    fresh+=1
                elif cur == 2:
                    queue.append((r,c))
        
        DIRECTIONS = [(0,-1),(0,1),(-1,0),(1,0)]

        while queue and fresh > 0:
            #think about timing 
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dr,dc in DIRECTIONS:
                    new_r = r + dr
                    new_c = c + dc

                    if(new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS):
                        continue

                    if grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append((new_r,new_c))
                        fresh -= 1 #rotten now


                #Go in all directions and add as needed
            time += 1
        
        return time if fresh == 0 else -1


        
                




        