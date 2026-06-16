class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        neighbors = defaultdict(list)

        for a,b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)
        
        
        heights = defaultdict(list)

        def dfs(num, parent):
            height = 1

            for nei in neighbors[num]:
                if nei == parent: continue
                
                height = max(height, 1 + dfs(nei,num))
            
            return height

        for num in range(n):
            heights[dfs(num,None)].append(num)
        

        return heights[min(heights)]


        