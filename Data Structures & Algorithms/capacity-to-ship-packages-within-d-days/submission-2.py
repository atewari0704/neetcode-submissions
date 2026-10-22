class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        # min = max(weights) max = sum(weights)

        # if days taken is less then d then lower the weigth capcpacity cuz we are able to move fast
        # if days taken is greater higher capcity 

        l = max(weights)
        r = sum(weights)

        res = r

        while l <= r:
            m = l+r//2

            # running sum kind of

            cur_load = 0
            days_taken = 0
            for w in weights:
                if w + cur_load > m:
                    days += 1
                    cur_load = w
                else:
                    cur_load += w

            days_taken += 1 # last load

            if days_taken == days:
                return m

            if days_taken < days:
                r = m - 1

                res = min(res,m)
            
            elif days_taken > days:
                l = m + 1
            

        return res 
        







        