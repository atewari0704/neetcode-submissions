class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        if len(coins) == 1:
            if amount % coins[0] == 0: return int(amount/coins[0])
            return -1
        
        #dynamic programming 
        dp = [amount+1] * (amount+1) # including 0 

        dp[0] = 0 # need 0 coins to make 0 dollars

        for i in range(1,len(dp)):
            for c in coins:
                leftover = i-c # given that we take out the current coin what do we need to make up
                if leftover >= 0:
                    dp[i] = min(dp[i],1 + dp[leftover])
        
        return dp[amount] if (dp[amount] != amount+1) else -1


