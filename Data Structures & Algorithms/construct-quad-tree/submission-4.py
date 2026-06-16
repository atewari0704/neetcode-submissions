"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def check_same(self, grid,rs,re,cs,ce):
        prev = None

        for i in range(rs,re):
            for j in range(cs,ce):
                cur = grid[i][j]
                if prev == None:
                    prev = cur
                
                if cur != prev:
                    new_grid = [temp[cs:ce] for temp in grid[rs:re]]
                    return self.construct(new_grid)
                
                prev = cur
        
        return Node(prev,1)

    def construct(self, grid: List[List[int]]) -> 'Node':
        ROWS,COLS = len(grid),len(grid[0])

        prev = grid[0][0]
        all_same = True

        for i in range(ROWS):
            for j in range(COLS):
                cur = grid[i][j]

                if cur != prev:
                    all_same = False
                    break
                    
        if all_same: return Node(prev,1)            

        root = Node(1,0)

        root.topLeft = self.check_same(grid, 0, ROWS//2, 0, COLS//2)

        root.topRight = self.check_same(grid, 0, ROWS//2, COLS//2, COLS)

        root.bottomLeft = self.check_same(grid, ROWS//2, ROWS, 0, COLS//2)

        root.bottomRight = self.check_same(grid, ROWS//2, ROWS, COLS//2, COLS)

        if root.topLeft == root.topRight == root.bottomLeft == root.bottomRight:
            return root.topLeft

        return root

        








        