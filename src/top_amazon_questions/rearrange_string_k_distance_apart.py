class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        counter = [0] * 26
        
        for c in s:
            counter[ord(c) - ord('a')] += 1
            
            
        last = [-float('inf')] * 26
        
        result = []
        
        for i, c in enumerate(s):
            
            best_c = None
            for j in range(26):
                if counter[j] and k <= i - last[j]:
                    if best_c is None or counter[best_c] < counter[j]:
                        best_c = j
                
            if best_c == None:
                return ''
            else:
                counter[best_c] -= 1
                result.append(chr(best_c + ord('a')))
                last[best_c] = i
            
        return ''.join(result)
