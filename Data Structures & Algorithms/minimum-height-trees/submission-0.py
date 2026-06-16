class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbors = defaultdict(list)

        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        
        heights = defaultdict(list)
        cur_visit = set()

        def dfs(num):
            height = 1
            cur_visit.add(num)

            for nei in neighbors[num]:
                if nei in cur_visit:
                    continue
                
                height = max(height, 1 + dfs(nei))
            
            cur_visit.remove(num)

            return height

        for num in range(n):
            heights[dfs(num)].append(num)
        

        return heights[min(heights)]


        