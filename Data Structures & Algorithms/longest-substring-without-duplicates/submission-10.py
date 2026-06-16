class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = dict() #letter:index

        l=0
        res = 0
        for r in range(len(s)):
            cur = s[r]

            if cur in visited:
                prev_i = visited[cur] # the index of the duplicate 

                while l <= prev_i:
                    print(visited)
                    del visited[ s[l] ] # remove everything up to the point of contention
                    l += 1

            #else:
            res = max(res,r - l + 1) # we can prob remove this
            visited[cur] = r 
        
        return res



        

