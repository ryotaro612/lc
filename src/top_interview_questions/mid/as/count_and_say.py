class Solution:
    def countAndSay(self, n: int) -> str:
        seq = [1]
        for _ in range(1, n):
            seq = self.convert(seq)
        return ''.join([str(item) for item in seq])
    
    def convert(self, seq):
        result = []
        start = 0
        peek = 0
        n = len(seq)
        while True:
            while peek < n and seq[start] == seq[peek]:
                peek += 1
            
            result.extend([peek - start, seq[start]])
            start = peek
            if peek == n:
                return result
            
