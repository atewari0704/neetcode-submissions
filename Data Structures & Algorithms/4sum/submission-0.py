class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res,quad = [],[]

        def kSum(k,start,target):
            # choose a value and the target decrements but so does the number of total values you have to choose
            if k > 2:
                for i in range(start,len(nums) - k + 1):
                    # don't want to use the same number over an over again
                    if i > start and nums[i] == nums[i - 1]:
                        continue 
                    quad.append(nums[i])
                    kSum(k-1,i + 1, target - nums[i])
                    quad.pop()

            #else base case with only 2 nums to choose 2sum II 
            else:
                l,r = start,len(nums)-1
                while l < r:
                    if nums[l] + nums[r] > target:
                        r -= 1
                    elif nums[l] + nums[r] < target:
                        l += 1
                    else:
                        res.append(quad + [nums[l],nums[r]])
                        l += 1

                        while l < r and nums[l] == nums[l-1]:
                            l += 1
        kSum(4,0,target)
        return res