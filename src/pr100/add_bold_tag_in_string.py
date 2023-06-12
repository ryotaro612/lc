class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        n = len(s)
        found = [False] * n
        for word in [word for word in words if n >= len(word)]:
            a = 0
            b = 0
            n_word = len(word)
            p = 100000000 + 7
            mod = 1 << 31
            for i in range(n_word):
                a = (a * p + ord(word[i])) % mod
                b = (b * p + ord(s[i])) % mod

            if a == b:
                for i in range(n_word):
                    found[i] = True
            t = 1
            for i in range(n_word - 1):
                t *= p
                t %= mod

            for i in range(n_word, n):
                b -= ord(s[i - n_word]) * t % mod
                b = (b * p + ord(s[i])) % mod
                if a == b:
                    for j in range(i - n_word + 1, i + 1):
                        found[j] = True
        # print(found)
        res = []
        for i, e in enumerate(found):
            if e:
                if i == 0 or i and found[i - 1] == False:
                    res.append("<b>")
                res.append(s[i])
                if i == n - 1 or found[i + 1] == False:
                    res.append("</b>")
            else:
                res.append(s[i])
        return "".join(res)
