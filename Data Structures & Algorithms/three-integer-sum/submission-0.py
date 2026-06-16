class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        if len(nums) == 3:
            if sum(nums) == 0:
                triplets.append(nums)
            return triplets
        
        nums.sort() # this takes of duplicates of triplets because we will only 
        # have sorted triplets now too

        for i,val in enumerate(nums):
            if val > 0 : break # because all the sums > 0 now
            if i > 0 and val == nums[i-1]:
                continue

            l = i + 1 
            r = len(nums) - 1

            while l < r:
                cur_sum = val + nums[l] + nums[r]
            
                if cur_sum < 0:
                    l += 1

                elif cur_sum > 0:
                    r -= 1
                
                elif cur_sum == 0:
                    triplets.append([val,nums[l],nums[r]])

                    # we could move up l if l+1 != l for values

                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1 # if it was the same as before then move it
        
        return triplets
                    
                



                



        
