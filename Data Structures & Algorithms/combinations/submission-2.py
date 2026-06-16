class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start,cur_combo):
            if len(cur_combo) == k:
                res.append(cur_combo[:])
                return # we can go back now and try to make a new combo
            
            if len(cur_combo) + (n - start + 1) < k: return # pruning because nothing from ehere onwards is long enough

            for i in range(start, n+1):
                cur_combo.append(i)

                backtrack(i+1,cur_combo) # we now want to add the next item if possible

                cur_combo.pop() # remove the last thing we added so we can get a new
                # unique combo
        
        backtrack(1,[])
        
        return res






























        # res = []

        # def backtrack(start,temp):
        #     if len(temp) == k:
        #         res.append(temp[:])
        #         return

        #     for i in range(start,n+1):
        #         temp.append(i)
        #         backtrack(i+1,temp)
        #         temp.pop()


        # backtrack(1,[])
        # return res

        