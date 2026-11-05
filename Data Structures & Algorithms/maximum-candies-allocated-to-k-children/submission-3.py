class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low,high = 0,max(candies)
        while low < high:
            middle = (low+high+1)//2
            portions = sum(x//middle for x in candies)
            if portions >= k: low = middle
            else: high = middle-1
        return low


        # def distribute(n):
        #     cur_candies = candies.copy()
        #     kids = k
        #     i = 0

        #     while i < len(cur_candies) and kids > 0:
        #         if cur_candies[i] >= n:
        #             cur_candies[i] -= n
        #             kids -= 1 # this kid got his n candy
        #         else:
        #             i += 1
            
        #     if kids > 0:
        #         # couldn't distribute successfully
        #         return False
            
        #     return True

        

        # l,r = 1,sum(candies)//k
        # res = 0

        # while l <= r:
        #     m = (l+r)//2

        #     if distribute(m):
        #         res = max(m,res)
        #         l = m+1

        #     else:
        #         r = m-1
        
        # return res




        



            




