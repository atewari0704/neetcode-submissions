class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def bs(row):
            l,r = 0,len(row)

            while l <= r:
                m = (l+r)//2

                if row[m] == target:
                    return True
                
                elif row[m] > target:
                    r = m - 1
                
                else:
                    l = m + 1
            
            return False
        

        for row in matrix:
            if target <= row[-1]:
                return bs(row)
        
        return False
        