import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_dict = dict()
        for task in tasks:
            task_dict.setdefault(task, 0)
            task_dict[task] += 1
        freq = [(-c, task) for task, c, in task_dict.items()]
        heapq.heapify(freq)
        result = 0
        i = 0
        last_process = dict()
        while True:
            # print(result, freq)
            temp = []
            for j in range(min(len(freq), n+1)):
                temp.append(heapq.heappop(freq))
                result += 1
            for count, name in temp:
                if count < -1:
                    heapq.heappush(freq, (count+1, name))
            if len(freq) == 0:
                return result
            if j < n:
                result += n - j
