class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def children(lock):
            res = []
            for i in range(4):
                inc = str( (int(lock[i]) + 1) % 10)
                res.append ( lock[:i] + inc + lock[i+1:] )
                dec = str( (int(lock[i]) + 9) % 10)
                res.append ( lock[:i] + dec + lock[i+1:] )
            return res
        


        visited = set(deadends)

        if "0000" in deadends: return -1


        q = deque([["0000",0]])

        
        while q:
            lock,turns = q.popleft()

            if lock == target:return turns

            for child in children(lock):
                if child in visited: continue

                q.append([child,turns+1])
                visited.add(child)
        
        return -1


         