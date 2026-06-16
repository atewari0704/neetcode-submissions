class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r = 0,len(nums) - 1

        # firsts step is actually built in which is to find the appropiate BS
        while l <= r:
            m = (l + r )//2

            if nums[m] == target: return True

            if nums[m] > nums[l]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else: # try to refine this
                    l = m + 1 
                
            elif nums[m] < nums[l]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else: # try to refine this
                    r = m - 1 
                
            else:
                l += 1 # because of duplicates this problem is harder 
        
        return False

        

        