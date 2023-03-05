from collections import deque

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        out_que, min_que, max_que, in_que = [deque() for _ in range(4)]
        n = len(nums)
        for i, num in enumerate(nums):
            if minK == num:
                min_que.append(i)
            if minK < num < maxK:
                in_que.append(i)
            if maxK == num:
                max_que.append(i)    
            if not (minK <= num <= maxK):
                out_que.append(i)

        out_que.append(n)
        
        result = 0
        
        for i, num in enumerate(nums):
            for que in [out_que, min_que, max_que, in_que]:
                while que and que[0] < i:
                    que.popleft()
            
            if not (minK <= num <= maxK):
                continue
            elif num == minK:
                if not max_que: 
                    continue
                result += max(0, out_que[0] - max_que[0]) 
            elif minK < num < maxK:
                if not max_que or not min_que:
                    continue
                result += max(0, out_que[0] - max(min_que[0], max_que[0]))
            elif num == maxK:
                if not min_que:
                    continue
                result += max(0, out_que[0] - min_que[0])

        return result
