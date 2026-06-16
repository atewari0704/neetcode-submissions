class TimeMap:
    def __init__(self):
        self.key_times = dict()
        self.key_vals = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not self.key_times.get(key,None):
            self.key_times[key] = []

        self.key_times[key].append(timestamp)

        self.key_vals[(key,timestamp)] = value # assuming only one key,timestamp pair
        
    def get(self, key: str, timestamp: int) -> str:
        times_array = self.key_times.get(key,None)

        #the time doesn't exist or the timestamp is smaller than the earliest time stamp
        if not times_array or times_array[0] > timestamp:
            return ""

        elif times_array[-1] <= timestamp:
            return self.key_vals[(key,times_array[-1])] # the most recent or exact same timestamp for key
        
        # do binary search
        else:
            lt_time = float("-inf") # lt stands for less than time which we can use
            l,r = 0,len(times_array)

            while l <= r:
                m = (l+r)//2

                cur_val = times_array[m]

                if cur_val == timestamp:
                    return self.key_vals[(key,cur_val)]
                
                elif cur_val > timestamp:
                    r = m - 1

                else:
                    lt_time = max(lt_time,cur_val)
                    l = m + 1
            
            if lt_time != float("-inf"):
                return self.key_vals[(key,lt_time)]
            
            return ""




        


        
