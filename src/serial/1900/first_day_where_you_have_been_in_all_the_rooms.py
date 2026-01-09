class Solution:
    def firstDayBeenInAllRooms(self, nextVisit: List[int]) -> int:
        """
        visit_counter = []
        time = []
        time[i]
        """
        n = len(nextVisit)
        counter = [0] * n
        day = 0
        cur = 0
        mod = 10**9 + 7
        for i in range(n):
            if i == 0:
                counter[0] = 0
                day = 2
            else:
                counter[i] = day
                day += day - counter[nextVisit[i]] + 2
                if day < 0:
                    day += mod
                day %= mod
        #print(counter)
        return counter[-1]
