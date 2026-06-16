class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0: return False

        length = sum(matchsticks)/4 # what the length of each side will be
        sides = [0] * 4


        matchsticks.sort(reverse=True)

        def bt(i):
            if i == len(matchsticks): return True

            for j in range(4):
                if sides[j] + matchsticks[i] <= length:
                    sides[j] += matchsticks[i]
                    if bt(i + 1):
                        return True
                    sides[j] -= matchsticks[i]
            return False
        
        return bt(0)
                    

        bt(0)


