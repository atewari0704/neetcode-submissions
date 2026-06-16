class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_taken(cur_k):
            hours = 0
            for num in piles: hours += math.ceil(num/cur_k)

            print(cur_k,hours)
            return hours


        l,r = math.ceil(sum(piles)/h), max(piles)

        while l <= r:
            m = int( (l+r)/2 )

            hours = hours_taken(m)

            if hours > h:
                l = m+1
            elif hours <= h:
                r = m-1
            # else:
            #     return m
                    
        return m

        # k = math.ceil(sum(piles)/h)

        # # Now we can make binary search
        # for possible_k in range(k,max(piles)+1):
        #     hours = 0

        #     for num in piles:
        #         hours += math.ceil(num/possible_k)

        #     if hours <= h: 
        #         return possible_k







        # # len_piles = len(piles)
        # k = float("inf")
        # visited = set()

        # idx = int(len_piles/2)

        # while idx not in visited:
        #     visited.add(idx)

        #     hours = 1 * (idx+1)
        #     cur = piles[idx]

        #     #may have to do some validation
        #     for i in range(idx+1,len_piles):
        #         hours += math.ceil(piles[i]/cur)
            
        #     if hours < h:
        #         k = min(k,cur)
        #         idx = int(idx/2)
            
        #     elif hours > h:
        #         idx = int((idx + len_piles)/2)
            
        #     else:
        #         return cur
        
        # return k



        