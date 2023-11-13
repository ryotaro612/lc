
from collections import defaultdict

class Solution:
    def sortVowels(self, s: str) -> str:
        letters = [c for c in s]
        vowels = defaultdict(int)
        vowel_set = {c for c in "AEIOUaeiou"}
        n = len(letters)
        for i in range(n):
            if letters[i] in vowel_set:
                vowels[letters[i]] += 1
        
        vowel_list = sorted([[letter,freq] for letter, freq in vowels.items()])
        v_i = 0
        for i in range(n):
            if letters[i] in vowel_set:
                letters[i] = vowel_list[v_i][0]
                vowel_list[v_i][1] -= 1
                if not vowel_list[v_i][1]:
                    v_i += 1
        
        return ''.join(letters)
