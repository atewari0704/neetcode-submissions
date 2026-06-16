class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subs = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i,len(nums)):
                if nums[i] < nums[j]:
                    subs[i] = max(subs[i], subs[j] + 1)


        return max(subs)       
