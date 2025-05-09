from collections import Counter
class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        
        counter = Counter([ord(c) - ord('0') for c in str(abs(num))])
        
        result = []
        if num > 0:

            for i in range(1, 10):
                if counter[i]:
                    result.append(i)
                    counter[i] -= 1
                    break
            for i in range(10):
                if counter[i]:
                    result.extend([i] * counter[i])
            
            return int(''.join([str(c) for c in result]))
        
        for i in range(9, -1, -1):
            if counter[i]:
                result.append(i)
                counter[i] -= 1
                break
        
        for i in range(9, -1, -1):
            if counter[i]:
                result.extend([i] * counter[i])
        
        return int(''.join([str(c) for c in result])) * -1
        
            
