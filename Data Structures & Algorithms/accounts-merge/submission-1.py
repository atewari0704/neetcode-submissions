class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        emailIdx = {} # email -> id
        emails = [] # set of emails of all accounts
        emailToAcc = {} # email_index -> account_Id

        m = 0
        for accId, a in enumerate(accounts):
            print(accId,a)
            for i in range(1, len(a)):
                email = a[i]
                if email in emailIdx:
                    continue
                emails.append(email)
                emailIdx[email] = m
                emailToAcc[m] = accId
                m += 1
        

        # making the intial adjacency list
        adj =[[] for _ in range(m)] #each email has it's own adjacency

        for a in accounts:
            for i in range(2,len(a)):
                adj1 = emailIdx[a[i]]
                adj2 = emailIdx[a[i-1]]

                adj[adj1].append(adj2)
                adj[adj2].append(adj1)
        

        emailGroup = defaultdict(list)
        visited = [False] * m
        def dfs(node,accId):
            visited[node] = True
            emailGroup[accId].append(emails[node]) # this account has this email 
            # if it was called in dfs

            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei,accId)

        for i in range(m):
            if not visited[i]:
                dfs(i,emailToAcc[i])
        

        res = []
        for accId in emailGroup:
            name = accounts[accId][0]
            res.append( [name] + sorted(emailGroup[accId]) )
        return res

                



        