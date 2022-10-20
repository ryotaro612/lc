"""
[1,3,-1,-3,5,3,6,7]
3
"""
import heapq

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        left = []
        right = []
        balance = 0
        n = len(nums)
        in_left = [False] * n
        
        for i in range(k):
            balance = self.put(i, k, nums, balance, in_left, left, right)
        
        result = []
        result.append(self.get(k, left, right))
        
        for i in range(k, n):
            balance = self.put(i, k, nums, balance, in_left, left, right)
            result.append(self.get(k, left, right))
            
        return result
    
    def put(self, i, k, nums, balance, in_left, left, right):
        if i - k >= 0:
            if in_left[i-k]:
                balance += 1
            else:
                balance -= 1
                
        if 0 <= balance:
            if right and right[0][0] < nums[i]:
                item = heapq.heappop(right)
                in_left[item[1]] = True
                heapq.heappush(left, (-item[0], item[1]))
                heapq.heappush(right, (nums[i], i))
            else:
                heapq.heappush(left, (-nums[i], i))
                in_left[i] = True
            balance -= 1
        else: # 0 > balance
            if nums[i] < -left[0][0]:
                item = heapq.heappop(left)
                in_left[item[1]] = False
                heapq.heappush(right, (-item[0], item[1]))
                in_left[i] = True
                heapq.heappush(left, (-nums[i], i))
            else:
                heapq.heappush(right, (nums[i], i))
            balance += 1
        
        for ary in [left, right]:
            while ary and ary[0][1] <= i - k:
                heapq.heappop(ary)
        # print(balance, i, left, right)
        return balance
    
    def get(self, k, left, right):
        if k % 2:
            return -left[0][0]
        else:
            return (-left[0][0] + right[0][0]) / 2
