class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        target = sum(nums)/2
        

        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1,-1, -1):
            num = nums[i]
            tempSet = set()

            for prevSum in dp:
                if num + prevSum == target:
                    return True

                if num + prevSum < target: 
                    tempSet.add(num + prevSum)

                tempSet.add(prevSum)
            
            dp = tempSet
        
        return False
        


        