"""
["let1 art zero can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
"""
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        for log in logs:
            if self.isDigitLog(log):
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        return sorted(letter_logs, key=self.sortLetterLogKey) + digit_logs
    
    def isDigitLog(self, log: str):
        index = log.find(" ")
        for c in log[index+1:]:
            if not c in self.digits and c != ' ':
                return False
        return True
    
    def sortLetterLogKey(self, log: str):
        index = log.find(' ')
        return (log[index+1:], log[:index])
        
    digits = set([str(i) for i in range(10)])
        
