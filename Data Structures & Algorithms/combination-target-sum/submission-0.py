class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # cur is the cur array with everything added until that point
        # total is the total of everthing that is currently in cur
        def dfs(i,cur,total):
            if total == target:
                res.append(cur[:])
                return
            
            elif total > target or i >= len(nums):
                return 

    
            # actually populate the cur
            cur.append(nums[i])
            #descision tree

            #add the same element again
            dfs(i,cur,total + nums[i])

            # we just added the element so lets remove it
            cur.pop() 

            dfs(i+1,cur,total)
        

        dfs(0,[],0)

        return res
        