class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        nums_len = len(nums)
        left = [1] * nums_len
        right = [1] * nums_len
        res = [1] * nums_len

        for i in range(1,nums_len):
            left[i] = nums[i-1]*left[i-1]
        
        for i in range(nums_len-2,-1,-1):
            print(i)
            right[i] = nums[i+1] * right[i+1]
        
        for i in range(0,nums_len):
            res[i] = left[i] * right[i]
        
        return res
        
        