class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        res_len = 1
        
        for i in range(len(s) - 1):
            l,r = i,i+1
            cur_res = ""
            cur_res_len = 0

            while l > -1 and r < len(s) and s[l] == s[r]:
                cur_res += s[r]
                cur_res = s[l] + cur_res
                cur_res_len += 2

                l -= 1
                r += 1
            if cur_res_len > res_len:
                res_len = cur_res_len
                res = cur_res
        

            l,r = i-1,i+1
            cur_res = s[i]
            cur_res_len = 1

            while l > -1 and r < len(s) and s[l] == s[r]:
                cur_res += s[r]
                cur_res = s[l] + cur_res
                cur_res_len += 2

                l -= 1
                r += 1
            if cur_res_len > res_len:
                res_len = cur_res_len
                res = cur_res
    
        return res