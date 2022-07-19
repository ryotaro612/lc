"""
 [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
 
"""
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        n = len(people)
        result = []
        bit = [0] * 1000002
        not_used = set(range(n))
        while len(not_used) > 0:
            candidate = None
            for i in not_used:
                h, k = people[i]
                if candidate is not None and people[candidate][0] < h:
                    continue
                count = n - len(not_used) - self.bit_sum(h, bit)
                # print(count)
                if count == k:
                    if candidate is None or h < people[candidate][0]:
                        candidate = i
            # print(candidate)
            
            self.bit_add(people[candidate][0] + 1, bit)
            result.append(people[candidate])
            not_used.remove(candidate)
        return result
    
    def bit_sum(self, i, bit):
        result = 0
        while i > 0:
            result += bit[i]
            i -= i & -i
        return result
    
    def bit_add(self, i, bit):
        while i < 1000002:
            bit[i] += 1
            i += i & -i
        
