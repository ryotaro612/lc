from collections import defaultdict
import heapq
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        n = len(nums)

        num_pos_ary = []
        for i, num in enumerate(nums):
            if num % 2:
                num_pos_ary.append([num, i])
                num_pos_ary.append([num*2, i])
            else:
                while num % 2 == 0:
                    num_pos_ary.append([num, i])
                    num //= 2
                num_pos_ary.append([num, i])
        
        num_pos_ary.sort()

        freq = defaultdict(int)
        result = float('inf')
        right = 0
        for left in range(len(num_pos_ary)):
            right = max(left, right)

            while right < len(num_pos_ary) and len(freq) < n:
                freq[num_pos_ary[right][1]] += 1
                right += 1
            if len(freq) == n:
                result = min(result, num_pos_ary[right-1][0] - num_pos_ary[left][0])
            
            freq[num_pos_ary[left][1]] -= 1
            if not freq[num_pos_ary[left][1]]:
                del freq[num_pos_ary[left][1]]
        return result
