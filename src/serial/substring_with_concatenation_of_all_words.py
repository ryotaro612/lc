"""
"barfoothefoobarman"
["foo","bar"]

"wordgoodgoodgoodbestword"
["word","good","best","word"]

"barfoofoobarthefoobarman"
["bar","foo","the"]

"wordgoodgoodgoodbestword"
["word","good","best","good"]
"""
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) < len(words[0]):
            return []
        
        word_freq = dict()
        for word in words:
            if word not in word_freq:
                word_freq[word] = 0
            word_freq[word] += 1
        
        result = []
        word_len = len(words[0])
        for i in range(word_len):
            count = len(words)
            freq = dict(word_freq)
            for cursor in range(i, len(s), word_len):
                substr = s[cursor:cursor + word_len]
                head_pos = cursor - word_len * (len(words)-count)
                head = s[head_pos:head_pos+word_len]
                # print(i, cursor, count, head)
                if substr in freq:
                    if freq[substr] > 0:
                        freq[substr] -= 1
                        count -= 1
                        if count == 0:
                            result.append(head_pos)
                            freq[head] = 1
                            count = 1
                    else:
                        while True:
                            if head == substr:
                                break
                            else:
                                freq[head] += 1
                                count += 1
                                head_pos += word_len
                                head = s[head_pos:head_pos+word_len]
                else:
                    count = len(words)
                    freq = dict(word_freq)
        return result
                        
                            
        
