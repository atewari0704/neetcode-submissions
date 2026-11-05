class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        pass

        # the max candy that can be given is the sum(candies)//k
        # the min candy is 1 and if that doesn't work then we return zero

        # the biggest issue is that once you take candy from one pile you can't use candy from another

        def distribute(n):
            cur_candies = candies.copy()
            kids = k
            i = 0

            while i < len(cur_candies) and kids > 0:
                if cur_candies[i] >= n:
                    cur_candies[i] -= n
                    kids -= 1 # this kid got his n candy
                else:
                    i += 1
            
            if kids > 0:
                # couldn't distribute successfully
                return False
            
            return True

        

        l,r = 1,sum(candies)//k
        res = 0

        while l <= r:
            m = (l+r)//2

            if distribute(m):
                print(m)
                res = max(m,res)
                l = m+1

            else:
                r = m-1
        
        return res




        



            




