from collections import defaultdict

class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr_words = defaultdict(set)
        for word in dictionary:
            self.abbr_words[self.abbr(word)].add(word)
        
    def isUnique(self, word: str) -> bool:
        abbr_word = self.abbr(word)
        if abbr_word not in self.abbr_words:
            return True
        elif len(self.abbr_words[abbr_word]) > 1:
            return False
        
        return word in self.abbr_words[abbr_word]
        
    def abbr(self, word):
        if len(word) <= 2:
            return word
        else:
            return word[0] + str(len(word[1:len(word) - 1])) + word[-1]


# Your ValidWordAbbr ob
