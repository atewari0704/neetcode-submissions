class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)] # for each i,j combo is the substring from i to j a plaindrome
        res_len = 1
        res_idx = 0

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i+1 > res_len:
                        res_len = j-i+1
                        res_idx = i
        
        return s[res_idx:res_idx+res_len]








        # res = s[0]
        # res_len = 1
        
        # for i in range(len(s) - 1):
        #     l,r = i,i+1
        #     cur_res = ""
        #     cur_res_len = 0

        #     while l > -1 and r < len(s) and s[l] == s[r]:
        #         cur_res += s[r]
        #         cur_res = s[l] + cur_res
        #         cur_res_len += 2

        #         l -= 1
        #         r += 1
        #     if cur_res_len > res_len:
        #         res_len = cur_res_len
        #         res = cur_res
        

        #     l,r = i-1,i+1
        #     cur_res = s[i]
        #     cur_res_len = 1

        #     while l > -1 and r < len(s) and s[l] == s[r]:
        #         cur_res += s[r]
        #         cur_res = s[l] + cur_res
        #         cur_res_len += 2

        #         l -= 1
        #         r += 1
        #     if cur_res_len > res_len:
        #         res_len = cur_res_len
        #         res = cur_res
    
        # return res