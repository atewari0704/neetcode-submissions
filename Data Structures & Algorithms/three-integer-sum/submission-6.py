class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 1):
            x = nums[i]
            l = i + 1
            r = len(nums) - 1

            while l < r:
                y = nums[l]
                z = nums[r]

                if x + y + z < 0:
                    l += 1
                
                elif x + y + z > 0:
                    r -= 1
                
                else:
                    res.append([x,y,z])
                    l += 1
                    r -= 1

                    while nums[l] == nums[l-1] and l < r:
                         l += 1

                


        