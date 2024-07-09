class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current = 0
        times = []
        for arrival, time in customers:
            if current <= arrival:
                times.append(time)
                current = arrival + time
            else:
                times.append(current - arrival + time)
                current += time
        return sum(times) / len(customers)
