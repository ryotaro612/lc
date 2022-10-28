"""
[1,0,1,1,0]
d = [-1, 1, 4]
max(d[i+1] - d[i] - 1) < answer 
d[i+2] - d[i] - 1

-1, 1, 4, 6
"""
from collections import deque
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        que = deque()
        que.append(-1)
        result = 0
        for i, num in enumerate(nums):
            if not num:
                que.append(i)
                temp = list(que)
                result = max(result, temp[1] - temp[0] - 1)
                if 2 < len(temp):
                    result = max(result, temp[2] - temp[0] - 1)
                    que.popleft()
        
        temp = list(que) + [len(nums)]
        
        result = max(result, temp[1] - temp[0] - 1)
        if 2 < len(temp):
            result = max(result, temp[2] -  temp[0] - 1)
        return result
            
