class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target: return 0  

        min_len = len(nums)

        l = 0

        cur_sum,cur_len = nums[l],1

        for r in range(1,len(nums)):
            if cur_sum < target:
                cur_sum += nums[r]
                cur_len += 1
            
            while cur_sum >= target:
                min_len = min(min_len,cur_len)

                cur_sum -= nums[l]
                l += 1
                cur_len -= 1
        
        return min_len

