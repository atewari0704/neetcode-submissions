class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start,end):
            if start == end: res.append(nums[:]) # append a copy of the cur nums perm

            for i in range(start,end):
                nums[start],nums[i] = nums[i], nums[start] # swap for the first time
                backtrack(start+1,end)
                nums[start],nums[i] = nums[i], nums[start] # swap back to "og"

        backtrack(0,len(nums))
        return res
        