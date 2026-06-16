class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def pali(i,j):
            while i <= j:
                if s[i] != s[j]: 
                    return False
                i += 1
                j -= 1
            
            return True

        def dfs(i):
            if i >= len(s):
                res.append(part[::])
                return 
            
            # see the valid palindrome subs you can make starting at a given i
            for j in range(i,len(s)):
                if pali(i,j):
                    part.append(s[i:j+1])
                    dfs(j+1) # go and make other pali sub from J+1 onwards
                    part.pop()
        

        dfs(0)
        return res


            














        dfs(0)
        return res











        # def is_pali(arr):
        #     for sub in arr:
        #         l,r = 0,len(sub)-1

        #         while l <= r:
        #             if sub[l] != sub[r]:
        #                 return False
        #             else:
        #                 l += 1
        #                 r -= 1
        #     return True


        # res = []

        # def bt(cur,i):
        #     if i >= len(s):
        #         if is_pali(cur): res.append(cur[::])
        #         return

        #     cur.append(s[i])
        #     bt(cur,i+1)
        #     cur.pop()

        #     if i != 0:
        #         cur[-1] = cur[-1]+s[i]
        #         bt(cur,i+1)


        # bt([],0)
        # return res        