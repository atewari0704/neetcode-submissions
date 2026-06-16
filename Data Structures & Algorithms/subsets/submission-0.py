class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        outcomes = [[]]

        for num in nums:
            temp = []

            for cur_item in outcomes:
                modified = cur_item.copy()
                modified.append(num)
                temp.append(modified)
            
            outcomes.extend(temp)
        
        return outcomes