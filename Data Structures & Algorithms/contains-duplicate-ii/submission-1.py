class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set()

        for i, val in enumerate(nums):
            if val in visited: return True
            
            visited.add(val) 

            if len(visited) > k:
                visited.remove(nums[i-k])
        
        return False
                



        # map = dict()

        # for i, val in enumerate(nums):
        #     if map.get(val) != None:
        #         prev_i = map[val]

        #         if i - prev_i <= k:
        #             return True
            
        #     map[val] = i

        # return False
        