class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        # devices = [3, 2, 1]
        result = 0
        """
        devices[i] * devices[i+1] + devices[i+1] * devices[i+2]...
        """
        prev = 0
        for row in bank:
            count = 0
            for c in row:
                if c == '1':
                    count += 1
            
            if count:
                if prev:
                    result += count * prev
                prev = count
        return result
                    
