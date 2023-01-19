"""
["Walnut","parseText","parseText","getAverageUserEarnings","getAverageUserEarnings"]
[[],[1,"deposited $100"],[2,"debit $500"],[],[]]

["Walnut","getTotalUserExpenses","getAverageUserExpenses"]
[[],[1],[]]

["Walnut","parseText","parseText","getTotalUserEarnings","getTotalUserExpenses","getAverageUserEarnings","getAverageUserExpenses"]
[[],[1,"credit $.01"],[2,"debit $1."],[1],[2],[],[]]
"""
import re
from collections import defaultdict

class Walnut:

    def __init__(self):
        self.earnings = defaultdict(int)
        self.expenses = defaultdict(int)
        self.earning_words = {"credit", "credited", "deposit", "deposited"}
        self.expense_words = {"debit", "debited", "withdraw", "withdrawal", "withdrawn"};
        self.sum_earnings = 0
        self.sum_expenses = 0
        self.users = set()
        
    def parseText(self, userID: int, text: str) -> None:
        print('pattern: ', text)
        result = self.parseEarning(text)
        # print('earn', result)
        if result is not None:
            self.earnings[userID] += result
            self.sum_earnings += result
            self.users.add(userID)
            return
        
        result = self.parseExpense(text)
        print('exep', result)
        if result is not None:
            self.expenses[userID] += result
            self.sum_expenses += result
            self.users.add(userID)
            return
        
    def parseEarning(self, text: str):
        words = set(text.split(' '))
        if words & self.earning_words and not words & self.expense_words:
            return self.extractPattern(text)
        
    def parseExpense(self, text: str):
        words = set(text.split(' '))
        if not words & self.earning_words and words & self.expense_words:
            print(text)
            return self.extractPattern(text)

    def extractPattern(self, text: str):
        """
        "USD x", "x USD", "USDx", "$ x", "x $", or "$x"
        """
        result = []
        for pattern in [r'USD ?(\d{1,10}(?:\.\d+)?)', r'(\d{1,10}(?:\.\d+)?) USD', 
                        r'\$ ?((?:\d{0,10})(?:\.\d+)?)', r'(\d{1,10}(?:\.\d+)?) \$']:
            money = self.extract_money(pattern, text)
            if money:
                result.append(money)
                
        if len(result) == 1:
            return result[0]
        else:
            return None
        
    def getTotalUserEarnings(self, userID: int) -> float:

        return self.earnings[userID]

    def getTotalUserExpenses(self, userID: int) -> float:
        return self.expenses[userID]

    def getAverageUserEarnings(self) -> float:
        if len(self.users):
            return self.sum_earnings / len(self.users)
        else:
            return 0
    
    def getAverageUserExpenses(self) -> float:
        if len(self.users):
            return self.sum_expenses / len(self.users)
        else:
            return 0
    
    def extract_money(self, pattern, text):
        found = re.findall(pattern, text)
        costs = [self.parse_num(value) for value in found]
        costs = [cost for cost in costs if cost is not None]
        if len(costs) == 1:
            return costs[0]
        return None
    
    def parse_num(self, value):
        dot = value.find('.')
        v = float(value)
        if dot == -1 and 0 <= v <= 1000000000:
            return v
        
        n = len(value)
        if n - 2 == dot or n - 3 == dot:
            return float(value)
        else:
            return None

# Your Walnut object will be instantiated and called as such:
# obj = Walnut()
# obj.parseText(userID,text)
# param_2 = obj.getTotalUserEarnings(userID)
# param_3 = obj.getTotalUserExpenses(userID)
# param_4 = obj.getAverageUserEarnings()
# param_5 = obj.getAverageUserExpenses()
