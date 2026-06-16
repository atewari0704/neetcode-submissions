class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_l = float("-inf")
        # max_area = float("-inf")

        # for l in range(len(heights)):
        #     if heights[l] < max_l: continue

        #     max_l = heights[l]

        #     for r in range(l,len(heights)):
        #         cur_area = (r-l) * min(heights[l],heights[r])
        #         max_area = max(cur_area,max_area)
        
        # return max_area


        res = 0
        l,r = 0,len(heights)-1

        while l < r:
            area = (r-l) * min(heights[l],heights[r])
            res = max(res,area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r-=1
        return res

        
        