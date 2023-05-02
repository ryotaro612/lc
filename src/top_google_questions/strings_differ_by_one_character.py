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
