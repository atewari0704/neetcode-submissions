class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        pos = []

        def collisons(neg_val):
            pos_val = pos.pop()
            while neg_val + pos_val < 0 and pos:
                pos_val = pos.pop()
            
            if neg_val + pos_val == 0: return

            if neg_val + pos_val > 0:
                pos.append(pos_val)

            else:
                res.append(neg_val)

        for num in asteroids:
            if num > 0:
                pos.append(num)
            
            elif num < 0 and pos:
                collisons(num) 
            
            else:
                res.append(num)
        
        return res + pos
        