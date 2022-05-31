class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        encoder = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        results = set()
        for word in words:
            enc = []
            for c in word:
                enc.append(encoder[ord(c) - ord('a')])
            
            results.add(''.join(enc))
        return len(results)
