class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #How do we keep track of count -> dict make sure we keep neg count
        count_dict = dict()

        for num in nums:
            count_dict[num] = count_dict.get(num,0) - 1

        counts_list = []

        for key,val in count_dict.items():
            counts_list.append( (val,key) )


        heapq.heapify(counts_list)

        print(counts_list)

        res = []

        while k != 0:
            res.append( heapq.heappop(counts_list)[1] )
            k -= 1
        
        return res



         #for key,val in dict we get tuples but find a way so that the
         # count val is the 1st item in the dict

         # then we use a heapq and heapify the ^ tuples list

         # start popping till we meet K