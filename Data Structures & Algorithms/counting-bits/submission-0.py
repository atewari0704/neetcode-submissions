class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)

        cur_domain = 1
        next_domain = cur_domain * 2

        for i in range(1,n+1):
            if i == next_domain:
                cur_domain = next_domain
                next_domain *= 2
            
            dp[i] = 1 + dp[i-cur_domain]

        return dp


        