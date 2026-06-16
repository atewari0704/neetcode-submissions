class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # l,r = 0,len(heights)-1

        max_l = float("-inf")
        max_area = float("-inf")

        for l in range(len(heights)):
            if heights[l] < max_l: continue

            max_l = heights[l]

            for r in range(l,len(heights)):
                cur_area = (r-l) * min(heights[l],heights[r])
                max_area = max(cur_area,max_area)
        
        return max_area


        
        