class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canShip(cap):
            curCap,ships = cap,1

            for w in weights:
                if curCap - w < 0:
                    ships += 1
                    curCap = cap
                curCap -= w

                if ships > days: return False
            
            return ships <= days
        

        l,r = max(weights),sum(weights)
        res = r

        while l <= r:
            cap = (l+r)//2

            if canShip(cap):
                res = min(res,cap)
                r = cap - 1
                
            else:
                l = cap+1
        
        return res

        