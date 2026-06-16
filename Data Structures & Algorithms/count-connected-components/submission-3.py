class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        hashmap = dict()

        for val1,val2 in edges:
            if not hashmap.get(val1):
                hashmap[val1] = []

            hashmap[val1].append(val2)

            if not hashmap.get(val2):
                hashmap[val2] = []

            hashmap[val2].append(val1)

            visited.add(val1)
            visited.add(val2)
        

        def dfs(node, traversed):
            traversed.add(node)

            # visited.remove(node)

            for child in hashmap[node]:
                if child not in traversed:
                    dfs(child,traversed)
                    
            del hashmap[node] # newly added
        

        connected = 0

        for node in visited:
            if node in hashmap:
                dfs(node,set())
                connected += 1

        if len(visited) != n:
            connected += n - len(visited)

        return connected

        