class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #[2,-2,4,-3]
        #[(2,2), (-2,-4), (4,-16), (48, -12)] #max,min we keep track of min because it could help
        # when we encounter another min

        res = nums[0]
        curMax,curMin = 1,1

        for num in nums:
            temp = curMax * num
            curMax = max(temp, num, curMin * num)
            curMin = min(temp, num, curMin * num)

            res = max(res, curMax)
        
        return res

