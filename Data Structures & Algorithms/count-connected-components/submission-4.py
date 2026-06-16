class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # disjoint union 
        parent = [i for i in range(n)] # each node is reprsented by it's index and the val is the parent

        rank = [1] * n # basically how large each component set is

        def find(node):
            cur = node
            while parent[cur] != cur:
                cur = parent[cur]
            return cur

            #get the parent


        components = n 
        for n1,n2 in edges:
            p1,p2 = find(n1),find(n2)

            if p1 == p2:
                continue 
                return 0 # no union was done because parents are the same
            
            else:
                # do a union based on rank
                if rank[p1] > rank[p2]:
                    parent[p2] = p1
                    rank[p1] += rank[p2]
                else:
                    parent[p1] = p2
                    rank[p2] += rank[p1]

                components -= 1
        
        return components


























        # visited = set()
        # hashmap = dict()

        # for val1,val2 in edges:
        #     if not hashmap.get(val1):
        #         hashmap[val1] = []

        #     hashmap[val1].append(val2)

        #     if not hashmap.get(val2):
        #         hashmap[val2] = []

        #     hashmap[val2].append(val1)

        #     visited.add(val1)
        #     visited.add(val2)
        

        # def dfs(node, traversed):
        #     traversed.add(node)

        #     # visited.remove(node)

        #     for child in hashmap[node]:
        #         if child not in traversed:
        #             dfs(child,traversed)
                    
        #     del hashmap[node] # newly added
        

        # connected = 0

        # for node in visited:
        #     if node in hashmap:
        #         dfs(node,set())
        #         connected += 1

        # if len(visited) != n:
        #     connected += n - len(visited)

        # return connected

        