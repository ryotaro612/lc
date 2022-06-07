"""
10
189
"""
class Solution:
    def findNthDigit(self, n: int) -> int:
        run_sum = 0
        i = 0
        while True:
            next_run_sum = run_sum + (i + 1)* pow(10, i) * 9 
            if  next_run_sum < n:
                run_sum = next_run_sum
                i+= 1
            else:
                break
        # print(run_sum)
        remain = n - run_sum
        d = pow(10, i) + remain // (i+1)
        
        # print('run_sum', run_sum, 'remain', remain,'i', i, 'd', d)
        pos = remain % (i+1)
        if pos == 0:
            return (d-1) % 10
        else:
            return int(str(d)[pos-1])
