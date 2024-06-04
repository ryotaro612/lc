class MagicDictionary:

    def __init__(self):
        pass

    def buildDict(self, dictionary: List[str]) -> None:
        self.dictionary = dictionary

    def search(self, searchWord: str) -> bool:
        cands = [word for word in self.dictionary if len(word) == len(searchWord)]
        for cand in cands:
            n = len(cand)
            count = 0
            for i in range(n):
                if cand[i] != searchWord[i]:
                    count += 1
            if count == 1:
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
