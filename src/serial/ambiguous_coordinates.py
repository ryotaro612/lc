class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        """
        n = len(s)-2
        n-1
        """
        n = len(s)
        cache = dict()
        result = []
        for i in range(2, n-1):
            left = self.build(s[1:i], cache)
            right = self.build(s[i:n-1], cache)
            for a in left:
                for b in right:
                    result.append(f"({a}, {b})")
        
        return result

    def build(self, s, cache):
        if s in cache:
            return cache[s]
        
        if len(s) == 1:
            cache[s] = [s]
            return cache[s]
        
        result = []

        if s[0] != '0':
            result.append(s)
        n = len(s)
        for i in range(1, n):
            if s[i:][-1] == '0':
                continue
            if len(s[:i]) > 1 and s[0] == '0':
                continue
            result.append(s[:i] + '.' + s[i:])
        
        return result
