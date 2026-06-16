class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        def spiral(matrix):
            print("Starting Matirx: ",matrix)
            print("Res cur ",res)
            if len(matrix) == 0: return

            for num in matrix[0]:
                res.append(num)

            for row in matrix[1:-1]:
                res.append(row[-1])
            
            for num in matrix[-1][::-1]: 
                if len(matrix) == 1: break # the first and last row are the same NO duplicates
                res.append(num)
            
            for row in matrix[1:-1][::-1]:
                if len(row) == 1: break
                res.append(row[0])
            
            matrix = matrix[1:-1]

            for i in range(len(matrix)):
                matrix[i] = matrix[i][1:-1]
                if len(matrix[i]) == 0: return

                
            
            spiral(matrix)
        
        spiral(matrix)
        return res







































        # res = []

        # while matrix:
        #     if matrix and matrix[0]: # if there is a first row
        #         first_row = matrix.pop(0)
        #         res.extend(first_row)

        #     else: # this means the matrix is empty or carries empty arrays
        #         return res
            
        #     for i in range(len(matrix)):
        #         if i == len(matrix) - 1: # if we are at the last row
        #             last_row = matrix.pop(-1)
        #             res.extend(last_row[::-1]) # put the last row backwards

        #         else:
        #             last_item = matrix[i].pop(-1)
        #             res.append(last_item)
            
            
        #     # now from the remaining matrix take the first col backwards

        #     if matrix and matrix[0]:
        #         first_items = []

        #         for row in matrix:
        #             first_items.append(row.pop(0))

        #         first_items.reverse()

        #         res.extend(first_items)

        # return res




             