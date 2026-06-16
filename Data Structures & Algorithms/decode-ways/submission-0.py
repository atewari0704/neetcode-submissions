class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        for i in range(len(s) - 1,-1,-1):
            if s[i] == "0":
                dp[i] = 0
                continue
    
            res = dp[i + 1] # adding just the singluar number alone

            if i + 1 < len(s) and (s[i]+ s[i+1] <= "26"):
                res += dp[i + 2]

            dp[i] = res
        
        return dp[0]

    