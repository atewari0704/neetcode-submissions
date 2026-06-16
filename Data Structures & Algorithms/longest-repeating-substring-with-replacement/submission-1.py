class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        res = 0 
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1 

            while (r-l+1) - max(count.values()) > k:
                count[s[l]] = count[s[l]] - 1 #the left moved so the letter with l count goes down
                l += 1
                
            res = max(res,r-l+1)
        
        return res
            
        






           




        