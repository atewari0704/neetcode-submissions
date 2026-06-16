class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = dict()

        for i,pos in enumerate(position):
            pos_speed[pos] = speed[i]
        

        position.sort()
        
        times = []
        for pos in position:
            time = (target - pos)/pos_speed[pos]
            times.append(time)
        
        print(times)
        
        # the first time is the time of the first pos and last time is the time of the last pos
        stack = [times.pop()] # the time of the car in the last pos

        while times:
            cur_time = times.pop()
            if cur_time < stack[-1]:
                stack.append(stack[-1]) # you can only go faster than the car in front of you
            else:
                stack.append(cur_time)
            
        fleets = set(stack) 
        return len(fleets)
            
        
        



            


        