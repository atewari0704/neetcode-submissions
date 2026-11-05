class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        total = sum(candies)

        if total < k:
            print("triggered")
            return 0


        def distribute(n):
            piles = 0 

            for c in candies:
                piles += c//k

                if piles >= k:
                    return True
            
            return False
            
        

        l,r = 1,(total//k)
        res = 0

        while l <= r:
            m = (l+r)//2

            if distribute(m):
                res = m
                l = m+1

            else:
                r = m-1
        
        return res




        



            




