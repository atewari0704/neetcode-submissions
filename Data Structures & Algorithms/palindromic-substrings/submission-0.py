class Solution:
    def countSubstrings(self, s: str) -> int:
        def is_palindrome(s):
            l,r = 0,len(s)-1

            while l <= r:
                if s[l] != s[r]: return False

                l += 1
                r -= 1                    
            
            return True
        
        count = 0 
        for i in range(len(s)):
            # for each start get all possible substrings
            for j in range(i+1,len(s)+1):
                if is_palindrome(s[i:j]): 
                    count += 1
        
        return count
           
        
        