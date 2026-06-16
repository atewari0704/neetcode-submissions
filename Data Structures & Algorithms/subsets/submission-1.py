class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start,path):
            result.append(path[:])

            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)

                path.pop()
        
        backtrack(0,[])
        
        return result




















        # outcomes = [[]]

        # for num in nums:
        #     temp = []

        #     for cur_item in outcomes:
        #         modified = cur_item.copy()
        #         modified.append(num)
        #         temp.append(modified)
            
        #     outcomes.extend(temp)
        
        # return outcomes