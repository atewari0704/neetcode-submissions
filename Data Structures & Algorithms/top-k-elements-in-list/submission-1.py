class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()

        # this will make the counts of the dict possible
        for num in nums: 
            counts[num] = counts.get(num,0) + 1
        

        res = []

        for num, freq in counts.items():
            if len(res) < k:
                heapq.heappush(res,(freq,num))

            elif freq > res[0][0]:
                heapq.heapreplace(res,(freq,num))
        
        return [num for freq,num in res]

    
        


























        # #How do we keep track of count -> dict make sure we keep neg count
        # counts = dict()

        # for num in nums:
        #     counts[num] = counts.get(num,0) - 1

        # counts = [(val,key) for key,val in counts.items()]

        # heapq.heapify(counts)

        # res = []

        # while k != 0:
        #     res.append( heapq.heappop(counts)[1] )
        #     k -= 1
        
        # return res



        #  #for key,val in dict we get tuples but find a way so that the
        #  # count val is the 1st item in the dict

        #  # then we use a heapq and heapify the ^ tuples list

        #  # start popping till we meet K