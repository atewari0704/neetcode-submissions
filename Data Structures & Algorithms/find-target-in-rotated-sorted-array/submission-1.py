class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l <= r:
            m = (l+r)//2

            if nums[m] == target: return m

            # in the left sorted
            if nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    r = m-1
                else:
                    l = m+1

            # in the right sorted
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
        return -1



        