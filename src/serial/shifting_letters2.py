class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        """
        prefix[i] = [0..i]
        prefix[i] - prefix[i-]
        [i, j, 1]
        prefix[i] += 1
        prefix[j+1] -= 1
        prefix[i+1] += prefix[i] in i..n
        """
        n = len(s)
        prefix = [0] * (n+1)
        for start, end , direction in shifts:
            if direction:
                prefix[start] += 1
                prefix[end+1] -= 1
            else:
                prefix[start] -= 1
                prefix[end+1] += 1

        for i in range(1, n):
            prefix[i] += prefix[i-1]
        
        print(prefix)
        
        result = [c for c in s]
        for i, c in enumerate(result):
            shift = prefix[i]

            pos = (ord(c) - ord('a') + 26 + shift) % 26
            result[i] = chr(pos + ord('a'))
        
        return ''.join(result)
