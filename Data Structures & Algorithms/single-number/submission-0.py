class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        res = 0 # techincally we do this in bits on paper but it automatically is done 
        # in not bits

        for num in nums:
            res ^= num

        return res

        