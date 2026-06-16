class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def hours_taken(cur_k):
            hours = 0
            for num in piles: hours += math.ceil(num/cur_k)

            return hours


        l,r = math.ceil(sum(piles)/h), max(piles)

        while l <= r:
            m = int( (l+r)/2 )

            hours = hours_taken(m)

            if hours > h:
                l = m+1
            else:
                r = m-1

                    
        return m
