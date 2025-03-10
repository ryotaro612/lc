from collections import deque
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        
        ques = [deque() for _ in range(6)]
        vowels = 'aeiou'
        result = 0
        right = 0
        n = len(word)
        for left in range(n):
            right = max(left, right)

            while right < n and not (len(ques[-1]) == k and word[right] not in vowels):
                if word[right] in vowels:
                    ques[vowels.find(word[right])].append(right)
                else:
                    ques[-1].append(right)
                right += 1

            if len(ques[-1]) == k and len([q for q in ques[:5] if q]) == 5:
                l = max([que[0] for que in ques[:5]])
                if ques[-1]:
                    l = max(l, ques[-1][-1])
                r = max(que[-1] for que in ques if que)
                result += r - l + 1
            
            for que in ques:
                if que and que[0] == left:
                    que.popleft()
            
        return result
