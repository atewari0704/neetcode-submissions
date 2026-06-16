class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i,a in enumerate(nums):
            if i != 0 and nums[i] == nums[i-1]:
                continue # we have already seen all possible combos with this

            l,r = i+1,len(nums)-1

            while l < r:
                three_sum = a + nums[l] + nums[r]

                if three_sum > 0:
                    r -= 1
                
                elif three_sum < 0:
                    l += 1
                
                else:
                    res.append([a,nums[l],nums[r]])

                    l += 1

                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        
        return res
                        






        # if aq is what it was in the last iteration then continue


        #left pointer should be right after a and right isthe lenlist -1 only go while l < r


        #check if a + l + r is > 0 < 0 or ==0

        # if a+l+r == 0 then move l to check for a new combo and make sure l is not what it was before only go while l < r
        