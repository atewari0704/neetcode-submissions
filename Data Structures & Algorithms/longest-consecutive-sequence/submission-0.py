class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        print(nums_set)

        max_count = 0

        for num in nums:
            count = 1

            cur = num - 1
            while cur in nums_set:
                nums_set.remove(cur)
                count += 1
                cur -= 1

            cur = num + 1
            while cur in nums_set:
                nums_set.remove(cur)
                count += 1
                cur += 1
            
            if num in nums_set:
                nums_set.remove(num)
                
            max_count = max(count,max_count)
        
        return max_count



        