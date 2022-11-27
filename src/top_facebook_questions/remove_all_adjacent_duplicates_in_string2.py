"""
"abcd"
2

"deeedbbcccbdaa"
3

"pbbcggttciiippooaais"
2
"""
from collections import defaultdict

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        stack = []
        counter = defaultdict(int)
        size = 0
        for c in s:
            stack.append(c)
            size += 1
            counter[c] += 1
            if k < size:
                if counter[stack[-size]] == 1:
                    del counter[stack[-size]]
                else:
                    counter[stack[-size]] -= 1
                size -= 1
            while True:
                if size < k or 1 < len(counter):
                    break
                else:
                    for _ in range(k):
                        stack.pop()
                    size = 0
                    counter = defaultdict(int)
                    for i in range(min(len(stack), k)):
                        counter[stack[-1-i]] += 1
                        size += 1
                    #print(stack, counter)
            
            # print(stack, counter, size)        
        
        return ''.join(stack)
            
