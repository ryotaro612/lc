from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.checkin = dict()  # id -> stationname, t
        self.times = defaultdict(int)  # key = [(start, end)]
        self.nums = defaultdict(int)  # key[(start, end)]

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, start_time = self.checkin.pop(id)
        key = (start, stationName)
        self.times[key] += t - start_time
        self.nums[key] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        return self.times[key] / self.nums[key]
