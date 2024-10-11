import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        n = len(times)
        heap = [i for i in range(n)]
        heapq.heapify(heap)
        
        events = [e for i, time in enumerate(times) for e in [[time[0], True, i], [time[1], False, i]]]
        events.sort()

        used = [False] * n
        friend_to_chair = [-1] * n
        for _, is_arrival, i in events:
            if is_arrival:
                while used[heap[0]]:
                    heapq.heappop(heap)

                used[heap[0]] = True
                if i == targetFriend:
                    return heap[0]
                
                friend_to_chair[i] = heap[0]

            else:
                used[friend_to_chair[i]] = False
                heapq.heappush(heap, friend_to_chair[i])
        
