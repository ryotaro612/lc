class Solution:
    def rotatedDigits(self, n: int) -> int:
        counter = 0
        for i in range(1, n+1):
            s = str(i)
            chunk = []
            ok = True
            mp = {'2': '5', '5': '2', '6': '9', '9': '6'}
            for c in s:
                if c in {'0', '1', '8'}:
                    chunk.append(c)
                elif c in mp:
                    chunk.append(mp[c])
                else:
                    ok = False
                    break

            if ok:
                if int(''.join(chunk)) != i:
                    counter+=1
        return counter
