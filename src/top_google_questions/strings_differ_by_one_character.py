"""    
class Solution:
    def differByOne(self, dicti: List[str]) -> bool:
        # l
        l = len(dicti[0])

        for i in range(l):
            subwords = set()
            for word in dicti:
                sub = word[0:i] + word[i + 1 :]
                if sub in subwords:
                    return True
                subwords.add(sub)
        return False
"""


class Solution:
    def differByOne(self, dicti: List[str]) -> bool:
        mod = 1000000007
        h = 1 << 64

        hv = []
        for word in dicti:
            v = 0
            for c in word:
                v *= mod
                v %= h
                v += ord(c) - ord("a")
                v %= h
            hv.append(v)

        l = len(dicti[0])
        for i in range(l):
            found = set()

            for j, word in enumerate(dicti):
                c = ord(word[i]) - ord("a")
                sub = hv[j] - c * self.modpow(mod, (l - 1 - i), h) % h
                if sub < 0:
                    sub += h
                if sub in found:
                    return True
                found.add(sub)
        return False

    def modpow(self, x, n, mod):
        res = 1
        while n:
            if n & 1:
                res *= x
                res %= mod
            x *= x
            x %= mod
            n >>= 1
        return res
