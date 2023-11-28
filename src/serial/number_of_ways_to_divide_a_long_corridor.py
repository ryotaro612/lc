
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        n_seats = 2
        result = 1
        mod = 10**9 + 7
        streak_plants = 0
        left = 0

        for i, item in enumerate(corridor):
            if item == 'S':
                left = i
                break
        right = len(corridor)
        for i in range(len(corridor)-1, -1, -1):
            if corridor[i] == 'S':
                right = i + 1
                break
        else:
            return 0
        for i in range(left, right):
            item = corridor[i]
            if item == 'S':
                if n_seats == 2:
                    n_seats = 1
                    result = result * (streak_plants + 1) % mod
                    streak_plants = 0
                else:
                    n_seats = 2
            else:
                if n_seats > 1:
                    streak_plants += 1
        if n_seats == 1:
            return 0
        return result * (streak_plants + 1 ) % mod
