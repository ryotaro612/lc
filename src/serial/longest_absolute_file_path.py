"""
"file1.txt\nfile2.txt\nlongfile.txt"

"""
from collections import deque
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        que = deque(input)
        result = 0 
        while True:
            result = max(result, self.traverse(que, 0))
            if que:
                que.popleft()
            else:
                break
        return result
        
    def traverse(self, que, depth):
        name = []
        while que:
            c = que.popleft()
            if c == '\n':
                que.appendleft(c)
                break
            else:
                name.append(c)

        # print(''.join(name), len(name), depth)
        if '.' in name:
            return len(name)
        
        result = 0
        while que:
            delimiter = []
            while que:
                c = que.popleft()
                if c in {'\n', '\t'}:
                    delimiter.append(c)
                else:
                    que.appendleft(c)
                    break
            if len(delimiter) == depth + 2:
                result = max(result, self.traverse(que, depth+1))
            else:
                while delimiter:
                    que.appendleft(delimiter.pop())
                break
        if result:
            return len(name) + 1 + result
        else:
            return 0
