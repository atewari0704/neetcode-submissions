class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        
        maxes = [0]*len(nums)
        maxes[0] = nums[0]
        maxes[1] = nums[1]

        for i in range(2,len(nums)):
            to_add = max(maxes[0:i-1])
            maxes[i] = to_add + nums[i]
        
        return max(maxes[-1],maxes[-2])

        

        