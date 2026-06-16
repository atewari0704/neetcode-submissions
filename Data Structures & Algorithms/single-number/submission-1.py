class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        # res = 0 # techincally we do this in bits on paper but it automatically is done 
        # # in not bits

        # for num in nums:
        #     res ^= num

        # return res

        count={}
        for num in nums:
            if num not in count:
                count[num]=0
            count[num]+=1
        
        for num in count:
            if count[num]==1:
                return num
        