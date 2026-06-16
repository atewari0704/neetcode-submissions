class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0

        for num in nums:
            if num not in nums_set:
                 continue

            count = 1

            l = num - 1
            while l in nums_set:
                nums_set.remove(l)
                count += 1
                l -= 1

            r = num + 1
            while r in nums_set:
                nums_set.remove(r)
                count += 1
                r += 1
            
            nums_set.remove(num)

            max_count = max(count,max_count)
        
        return max_count



        