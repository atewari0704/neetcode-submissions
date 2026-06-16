class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_pali(arr):
            for sub in arr:
                l,r = 0,len(sub)-1

                while l <= r:
                    if sub[l] != sub[r]:
                        return False
                    else:
                        l += 1
                        r -= 1
            return True


        res = []

        def bt(cur,i):
            if i >= len(s):
                if is_pali(cur): res.append(cur[::])
                return

            cur.append(s[i])
            bt(cur,i+1)
            cur.pop()

            if i != 0:
                cur[-1] = cur[-1]+s[i]
                bt(cur,i+1)


        bt([],0)
        return res        