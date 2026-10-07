class UnionFind(object):
    def __init__(self,n):
        self.parent=[i for i in range(n)]
    
    def find(self, x):
        if x != self.parent[x]:
            return self.find(self.parent[x])
        return x
    def union(self, x, y):
        self.parent[self.find(y)] = self.find(x)
        return True

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        uf = UnionFind(len(accounts))
        rLookup = {}
        for index, account in enumerate(accounts):
            for email in account[1:]:
                if email in rLookup:
                    uf.union(rLookup[email], index)
                else:
                    rLookup[email] = index
        
        merged = {}
        for email, i in rLookup.items():
            leader = uf.find(i)
            if leader in merged:
                merged[leader].append(email)
            else:
                merged[leader] = [email]
        res = []
        for index, emails in merged.items():
            account = [accounts[index][0]] + sorted(emails)
            res.append(account)
        return res
        