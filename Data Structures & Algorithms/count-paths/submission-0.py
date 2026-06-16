class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        queue = deque([(0,0)])

        while queue:
            i,j = queue.pop()

            if i == m-1 and j == n-1:
                count += 1
                continue
            
            if i+1 < m:
                queue.append((i+1,j)) # down
            
            if j+1 < n:
                queue.append((i,j+1)) # left
        
        return count


        