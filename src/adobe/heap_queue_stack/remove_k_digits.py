"""
Example 1
n = len(num) = 7 
k = 3
select n - k = 4 digits

select the smallest one but not zero from num[0] to num[3]
select 1 at 0th
select the smallest one from num[1] to num[4]
select 2 at 3th
seleclt the smallest one from num[4] to num[5]
"""
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        ques = [deque() for _ in range(10)]
        n = len(num)
        for i in range(n):
            ques[int(num[i])].append(i)
        result = []
        start, end = 0, k + 1
        for i in range(n - k):
            for que in ques:
                while len(que) > 0 and que[0] < start:
                    que.popleft()
            
            for j, que in enumerate(ques):
                if len(que) > 0 and start <= que[0] and que[0] < end:
                    if not (len(result) == 0 and j == 0):
                        result.append(j)
                    start = que.popleft() + 1
                    # print(result[-1], start, end)
                    break
            end += 1
        if len(result) == 0:
            return "0"
        return ''.join([str(d) for d in result])
                
                
