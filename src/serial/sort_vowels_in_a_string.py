lass Solution:
    def sortVowels(self, s: str) -> str:
        letters = [c for c in s]
        vowels = []
        vowel_set = {c for c in "AEIOUaeiou"}
        n = len(letters)
        for i in range(n):
            if letters[i] in vowel_set:
                vowels.append(letters[i])
        
        vowels.sort()
        v_i = 0
        for i in range(n):
            if letters[i] in vowel_set:
                letters[i] = vowels[v_i]
                v_i += 1
        
        return ''.join(letters)
