"""
["alice,20,800,mtv","bob,50,1200,mtv","alice,20,800,mtv","alice,50,1200,mtv","alice,20,800,mtv","alice,50,100,beijing"]

["bob,656,1366,bangkok","bob,820,990,amsterdam","alex,596,1390,amsterdam"]

["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]

"""
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        acc_trans = dict()
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time = int(time)
            if name not in acc_trans:
                acc_trans[name]=dict()
                
            if time not in acc_trans[name]:
                acc_trans[name][time] = set()
            
            acc_trans[name][time].add(city)
        result = []        
        for transaction in transactions:
            name, time, amount, city = transaction.split(',')
            time, amount = int(time), int(amount)
            if amount > 1000:
                result.append(transaction)
                continue
            
            for i in range(time - 60, time + 60 + 1):
                if i in acc_trans[name]:
                    if len(acc_trans[name][i]) > 1 or city not in acc_trans[name][i]:
                        result.append(transaction)
                        break
        return result
                        
