from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        heap = [[-freq, letter] for letter, freq in Counter(s).items()]
        heapq.heapify(heap)
        result = [' ']
        
        while heap:
            # print(heap, result)
            if heap[0][1] != result[-1]:
                freq, letter = heapq.heappop(heap)
                result.append(letter)
                if freq < -1:
                    heapq.heappush(heap, [freq+1, letter])
            else:
                top = heapq.heappop(heap)
                if heap:
                    freq, letter = heapq.heappop(heap)
                    result.append(letter)
                    if freq < -1:
                        heapq.heappush(heap, [freq+1, letter])
                    heapq.heappush(heap, top)
                else:
                    return ''

        return ''.join(result)[1:]
