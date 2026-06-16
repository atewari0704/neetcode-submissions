class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS,COLS = len(board),len(board[0])

        #instead of trying to capture surronded just capture Unsorrounded
        #because then everything that is NOT Unsurrounded is technically X

        def capture(r,c):
            if (r < 0 or r==ROWS or c<0 or c==COLS
                or board[r][c] != "O"):
                return
            
            # it means that this is a "O"
            board[r][c] = "T"

            capture(r+1,c)
            capture(r-1,c)
            capture(r,c+1)
            capture(r,c-1)
        

        #Capture the unsurronding regions
        for r in range(ROWS):
            if r == 0 or r == ROWS-1:
                for c in range(COLS):
                    capture(r,c)
            else:
                capture(r,0) # first col
                capture(r,COLS-1) # last col
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                
                elif board[r][c] == "T":
                    board[r][c] = "O"
                
        
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         ROWS, COLS = len(board), len(board[0])

#         def capture(r, c):
#             if (r < 0 or c < 0 or r == ROWS or
#                 c == COLS or board[r][c] != "O"
#             ):
#                 return
#             board[r][c] = "T"
#             capture(r + 1, c)
#             capture(r - 1, c)
#             capture(r, c + 1)
#             capture(r, c - 1)

#         for r in range(ROWS):
#             if board[r][0] == "O":
#                 capture(r, 0)
#             if board[r][COLS - 1] == "O":
#                 capture(r, COLS - 1)

#         for c in range(COLS):
#             if board[0][c] == "O":
#                 capture(0, c)
#             if board[ROWS - 1][c] == "O":
#                 capture(ROWS - 1, c)

#         for r in range(ROWS):
#             for c in range(COLS):
#                 if board[r][c] == "O":
#                     board[r][c] = "X"
#                 elif board[r][c] == "T":
#                     board[r][c] = "O"



