class Solution:
    def intToRoman(self, num: int) -> str:
        map = {
            1000 :["","M","MM","MMM"],
            100: ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"],
            10:["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"],
            1:["","I","II","III","IV","V","VI","VII","VIII","IX"]
        }
        res = ""

        for pos in [1000,100,10,1]:
           res += map[pos][num//pos]
           num %= pos
        
        return res
        