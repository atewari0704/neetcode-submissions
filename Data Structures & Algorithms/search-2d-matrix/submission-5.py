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
        
        top,bottom = 0,len(matrix)-1

        while top <= bottom:
            m = (top + bottom)//2

            if target > matrix[m][-1]:
                top = m + 1
            
            elif target < matrix[m][0]:
                bottom = m - 1
            
            else:
                return bs(matrix[m])

        return False
        