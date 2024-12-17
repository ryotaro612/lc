from collections import Counter
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        result = []
        counter = Counter(s)
        freq = [[l, f] for l, f in counter.items()]
        
        freq.sort()

        while freq:
            l, f = freq.pop()
            if result:
                if result[-1] == l:
                    if freq:
                        l2, f2 = freq.pop()
                        result.append(l2)
                        if f2 > 1:
                            freq.append([l2, f2-1])

                        freq.append([l, f])
                        continue
                    else:
                        break
            
            n = min(f, repeatLimit)
            result.extend([l] * n)
            if n < f:
                freq.append([l, f-n])
            
        return ''.join(result)



            
    
