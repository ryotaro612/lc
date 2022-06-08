"""
counter = {'foo': 1, 'bar': 1}
count = 2 
"|barfoothefoobarman"
"|bar|foothefoobarman"
count = 1
couter  = {'foo': 1}
"|barfoo|thefoobarman"
counter = {}
count = 0
""bar|foo|thefoobarman""
counter = {'bar': 1}
count = 1

"lingmindraboofooowingdingbarrwingmonkeypoundcake"
["fooo","barr","wing","ding","wing"]

"barfoofoobarthefoobarman"
["bar","foo","the"]

"wordgoodgoodgoodbestword"
["word","good","best","word"]
"""
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        counter = dict()
        for word in words:
            counter.setdefault(word, 0)
            counter[word] += 1
        count = len(words)
        n = len(s)
        result = []
        w_len = len(words[0])
        for start in range(w_len):
            left, right = 0, 0
            for left in range(start, n, w_len):
                right = max(right, left)

                while right + w_len <= n and count > 0:
                    next_word = s[right:right+w_len] 
                    if counter.get(next_word, 0) > 0:
                        count -= 1
                        counter[next_word] -= 1
                        right += w_len
                    else:
                        break
                if count == 0:
                    result.append(left)

                if left < right:
                    left_word = s[left:left+w_len]
                    if left_word in counter:
                        counter[left_word] += 1
                        count += 1
        return result
