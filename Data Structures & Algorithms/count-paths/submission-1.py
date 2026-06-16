class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n # the bottom row is all 1's to start off

        for i in range(m-1):
            new_row = [1] * n
            # go through every col
            for j in range(n-2,-1,-1):
                new_row[j] = new_row[j+1] + row[j]
            row = new_row #the bottom row for the next iter is the row we just populated
        
        return row[0]




        # count = 0
        # queue = deque([(0,0)])

        # while queue:
        #     i,j = queue.pop()

        #     if i == m-1 and j == n-1:
        #         count += 1
        #         continue
            
        #     if i+1 < m:
        #         queue.append((i+1,j)) # down
            
        #     if j+1 < n:
        #         queue.append((i,j+1)) # left
        
        # return count


        