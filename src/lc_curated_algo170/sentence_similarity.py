from collections import defaultdict
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        n1 = len(sentence1)
        n2 = len(sentence2)
        if n1 != n2:
            return False
        
        sim_dict = defaultdict(set)

        for word1, word2 in zip(sentence1, sentence2):
            sim_dict[word1].add(word1)
            sim_dict[word2].add(word2)

        for word1, word2 in similarPairs:
            sim_dict[word1].update({word1, word2})
            sim_dict[word2].update({word1, word2})
        
        for word1, word2 in zip(sentence1, sentence2):
            if not word2 in sim_dict[word1]:
                return False

        return True
