class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS = len(board),len(board[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)] # u,d,l,r

        def dfs(idx, word_idx, parent_idx, visited):
            r,c = idx # destructing
            visited.add( (r,c) )

            if word_idx + 1 >= len(word):
                return True
            
            for rc,cc in directions:
                #if reusing parent
                if (r + rc < 0 
                    or r + rc >= ROWS 
                    or c + cc < 0
                    or c + cc >= COLS):
                    continue
                
                # if reusing parent
                if  (r+rc,c+cc) in visited:
                    continue
                
                if board[r+rc][c+cc] == word[word_idx+1]:
                    if dfs((r+rc,c+cc), word_idx + 1, idx, visited.copy()):
                        return True
            
            return False


        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs((r,c),0,None,set()): return True
                


        return False