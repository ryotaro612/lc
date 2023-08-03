from collections import deque
class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:
        n = len(arrival)
        result = [None] * n
        i = 0
        wait_enter = deque()
        wait_exit = deque()
        prev = 0
        sec = 0
        while sec <= arrival[-1] or wait_enter or wait_exit:
            while i < n and arrival[i] <= sec:
                if state[i] == 0:
                    wait_enter.append(i)
                else:
                    wait_exit.append(i)
                i += 1

            if prev in {0, 2}:
                first, second = wait_exit, wait_enter
            elif prev:
                first, second = wait_enter, wait_exit

            if first:
                result[first.popleft()] = sec
                if first is wait_exit:
                    prev = 2
                else:
                    prev = 1
            elif second:
                result[second.popleft()] = sec
                if second is wait_exit:
                    prev = 2
                else:
                    prev = 1
            else:
                prev = 0

            sec += 1
        return result
