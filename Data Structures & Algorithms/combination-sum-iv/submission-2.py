class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = {num:0 for num in range(1,target + 1)}
        dp[0] = 1

        for cur_target in range(1,target + 1):
            for num in nums:
                dp[cur_target] += dp.get(cur_target - num,0)

        return dp[target]




        # nums.sort()
        # res = 0

        # def bt(cur_target):
        #     nonlocal res
        #     for num in nums:
        #         if num == cur_target:
        #             res += 1
        #             return
                
        #         elif num < cur_target:
        #             bt(cur_target - num)
                
        #         else:
        #             return
        
        # bt(target)
        # return res
