class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        """
        12 -> 0
        h = hour * 5  + 5 * minutes / 60

        max(h, minutes) - min(h, minutes)
        60 + min(h, minutes) - max(h, minutes)

        360
        """
        hour_a = (hour % 12) * 5 + 5 * minutes / 60

        hour_a = 360 * hour_a / 60
        minutes_a = 360 * minutes / 60

        mini = min(hour_a, minutes_a)
        maxi = max(hour_a, minutes_a)
        
        point = min(maxi-mini, mini + 360 - maxi)
        return point
