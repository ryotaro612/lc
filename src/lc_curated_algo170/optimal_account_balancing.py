"""
[[2,0,5],[3,4,4]]
一回のトランザクションで最低ひとり、最高ふたりをバランスさせられる。
したがって、ひとりもバランスできないとりひきを考える必要はない。
"""
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        
        debts = [0] * (1 + max([max(t[:-1]) for t in transactions]))
        for giver, taker, amount in transactions:
            debts[giver] -= amount
            debts[taker] += amount
        
        print(debts)
        return self.rec(debts, 0)
    
    def rec(self, debts, person):
        n = len(debts)
        if person == n:
            return 0
        if debts[person] == 0:
            return self.rec(debts, person + 1)
        
        result = float('inf')
        for i in range(person + 1, n):
            if debts[person] * debts[i] < 0:
                debts[i] += debts[person]
                
                result = min(result, 1 + self.rec(debts, person + 1))
                
                debts[i] -= debts[person]
        # print(result, debts, person)
        return result
                
