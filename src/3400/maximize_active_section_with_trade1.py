class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        """
        [(0, 1), (1, 1), (0, 2)]
        
        [(0, a), (1, b), (0, c)] => result = max(result, a + b + c)
        """
        encoded = []
        counter = 0
        if s[0] == '0':
            encoded.append([0, 1])
        else:
            encoded.append([1, 1])

        n = len(s)
        for i in range(1, n):
            if s[i] == '0':
                if encoded[-1][0] == 0:
                    encoded[-1][1] += 1
                else:
                    encoded.append([0, 1])
            else:
                if encoded[-1][0] == 1:
                    encoded[-1][1] += 1
                else:
                    encoded.append([1, 1])
        
        base = 0
        for active, freq in encoded:
            if active:
                base += freq
        
        result = base
        for i in range(1, len(encoded)-1):
            if encoded[i][0] == 1:
                result = max(result, encoded[i-1][1] + base + encoded[i+1][1])
        
        return result
