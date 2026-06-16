class Solution:
    def numSquares(self, n: int) -> int:
        dp =[n] * (n+1)
        dp[0] = 0

        for target in range(1,n+1):
            for s in range(1,target+1):
                ps = s**2

                if ps > target:
                    break
                
                remainder = target - ps 
                dp[target] = min(dp[remainder] + 1 , dp[target])
            
        return dp[-1]

            