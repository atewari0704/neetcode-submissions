class Solution:
    def countSubstrings(self, s: str) -> int:
        def check_outward(l,r):
            count = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
            
            return count

        count = 0

        for i in range(len(s)):
            #check odd palindrome
            l = r = i
            count += check_outward(l,r)
            
            #even palindroms
            l,r= i,i+1
            count += check_outward(l,r)
            
        
        return count

            








        # def is_palindrome(s):
        #     l,r = 0,len(s)-1

        #     while l <= r:
        #         if s[l] != s[r]: return False

        #         l += 1
        #         r -= 1                    
            
        #     return True
        
        # count = 0 
        # for i in range(len(s)):
        #     # for each start get all possible substrings
        #     for j in range(i+1,len(s)+1):
        #         if is_palindrome(s[i:j]): 
        #             count += 1
        
        # return count
           
        
        