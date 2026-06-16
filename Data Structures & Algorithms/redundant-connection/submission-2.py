class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = dict()

        for v1,v2 in edges:
            if v1 not in adj_list:
                adj_list[v1] = []
            adj_list[v1].append(v2)

            if v2 not in adj_list:
                adj_list[v2] = []
            adj_list[v2].append(v1)


        visiting = set()

        def find_latest():
            l1,l2=None,None
            for v1,v2 in edges:
                if v1 in visiting and v2 in visiting:
                    l1,l2=v1,v2
            
            return [l1,l2]


        def dfs(cur,parent):
            visiting.add(cur)
            visiting.add(parent)

            for nei in adj_list[cur]:
                if parent == nei:
                    continue
                
                if nei in visiting:
                    return True
                
                if dfs(nei,cur): return True
            
            # if we didn't cause a cycle then remove from visited
            visiting.remove(cur)
            # visiting.remove(parent)
            return False
        

        for v1,v2 in edges:
            if dfs(v1,v2):
                return find_latest()
            visiting = set() # reset what we are currently visiting


