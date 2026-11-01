class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = [False for num in nums]
        reach[-1] = True # you can reach the last index by being at it 


        for i in range(len(nums)-2,-1,-1):
            if nums[i] == 0:
                continue #reach is false from that index

            for jump in range(nums[i],-1,-1):
                #is the jump in range
                if (i + jump) >= len(nums):
                    reach[i] = True
                    break
                
                if reach[i + jump]:
                    reach[i] = True
                    break
        

        return reach[0]
                
                

                
                



        
        