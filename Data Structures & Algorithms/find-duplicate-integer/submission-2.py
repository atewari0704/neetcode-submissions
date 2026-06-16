class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for num in nums:
            i = abs(num) - 1 # the index to mark as negative

            if nums[i] < 0:
                return abs(num) # you are a duplicate and this was already marked negative 
            
            nums[i] *= -1
        
        return -1 # will never get here but need to have a default retunr cuz we need to return an int
        