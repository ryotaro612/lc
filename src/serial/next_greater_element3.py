from collections import defaultdict
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        s = str(n)
        freq = defaultdict(int)

        for i in range(len(s) -1, -1, -1):
            d = ord(s[i]) - ord('0')
            for larger in range(ord(s[i]) - ord('0') + 1, 10):
                if freq[larger]:
                    follow = str(larger)
                    freq[larger] -= 1
                    freq[d] += 1
                    for v in range(10):
                        follow += str(v) * freq[v]
                    
                    result = int(s[:i]+ follow)
                    if result <= (1<<31) - 1:
                        return result
                    else:
                        return -1
            
            freq[d] += 1
        
        return -1
