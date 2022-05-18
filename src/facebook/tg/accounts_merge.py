"""
[["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
"""
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        account_map = dict()
        
        for account in accounts:
            name = account[0]
            if name not in account_map:
                account_map[name] = []
            account_map[name].append(account)
            
        result = []
        for name in account_map:
            par = dict()
            for account in account_map[name]:
                for i in range(1, len(account)):
                    if account[i] not in par:
                        par[account[i]] = account[i]
                    if i > 1:  
                        self.unite(account[i], account[i-1], par)
            mails = dict()
            for account in account_map[name]:
                for email in account[1:]:
                    rep_mail = self.find_root(email, par)
                    if rep_mail not in mails:
                        mails[rep_mail] = []
                    mails[rep_mail].append(email)
            for email in mails:
                result.append([name] + sorted(set(mails[email])))
        return result 
                    
            
        return result
    def find_root(self, a, par):
        if par[a] == a:
            return a
        par[a] = self.find_root(par[a], par)
        return par[a]
    def is_same(self, a, b, par):
        return self.find_root(a, par) == self.find_root(b, par)
    
    def unite(self, a, b, par):
        if self.is_same(a, b, par):
            return
        
        root_a = self.find_root(a, par)
        root_b = self.find_root(b, par)
        par[root_a] = root_b
        return
        
                        
