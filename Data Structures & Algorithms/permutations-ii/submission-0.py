class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        count = dict()

        for n in nums:
            count[n] = count.get(n,0) + 1
        

        def dfs():
            if len(perm) == len(nums):
                res.append(perm[::])

            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    dfs()
                    perm.pop()
                    count[n] += 1





        dfs()
        return res
        