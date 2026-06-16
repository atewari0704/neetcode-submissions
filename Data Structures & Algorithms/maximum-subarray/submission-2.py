class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # for i in range(1,len(nums)):
        #     nums[i] = max(nums[i],nums[i]+nums[i-1])
        
        # return max(nums)

        max_sum = nums[0]
        cur_sum = 0

        for n in nums:
            if cur_sum <= 0: cur_sum = 0

            cur_sum += n
            max_sum = max(max_sum,cur_sum)

        return max_sum


        