class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        x = len(nums) - k + 1

        res = None 

        for i in range(x):
            res = heapq.heappop(nums)
        
        return res
        