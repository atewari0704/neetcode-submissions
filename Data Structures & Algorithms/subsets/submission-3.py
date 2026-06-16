class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset[:])
                return

            # deciding to keep the i and try to move to the next
            subset.append(nums[i])
            dfs(i+1)

            # deciding not keep this i anymore
            subset.pop()
            dfs(i+1)

        dfs(0)

        return res

    




        # result = []

        # def backtrack(start,path):
        #     result.append(path[:])

        #     for i in range(start,len(nums)):
        #         path.append(nums[i])
        #         backtrack(i+1,path)

        #         path.pop()
        
        # backtrack(0,[])

        # return result














        # outcomes = [[]]

        # for num in nums:
        #     temp = []

        #     for cur_item in outcomes:
        #         modified = cur_item.copy()
        #         modified.append(num)
        #         temp.append(modified)
            
        #     outcomes.extend(temp)
        
        # return outcomes