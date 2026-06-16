class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        def bt(start, end, target, res):
            for i in range(start,end):
                new_target = target - nums[i]

                if nums[i] == 0 or new_target < 0: continue

                if new_target == 0:
                    res.append(nums[i])
                    nums[i] = 0
                    return True

                if bt(i + 1, end, new_target, res):
                    res.append(nums[i])
                    nums[i] = 0
                    return True

            return False
        

        target = sum(nums)/k
        if not target.is_integer(): return False
        subarrays = []


        for i in range(0,len(nums)):
            if nums[i] == 0: 
                continue
            
            if nums[i] == target: 
                subarrays.append([nums[i]])
                nums[i] = 0 
                continue

            cur_sub = []

            if bt(i+1,len(nums),target - nums[i],cur_sub):
                cur_sub.append(nums[i])
                subarrays.append(cur_sub)

            else:
                return False
        
        print(subarrays)
        return len(subarrays) == k




        