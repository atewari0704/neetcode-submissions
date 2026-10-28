class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0

        def bt(cur_target):
            nonlocal res
            for num in nums:
                if num == cur_target:
                    res += 1
                
                elif num < cur_target:
                    bt(cur_target - num)
                
                else:
                    return
        
        bt(target)
        return res
