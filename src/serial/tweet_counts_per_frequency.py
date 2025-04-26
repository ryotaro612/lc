from collections import defaultdict

class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(list)        

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].append(time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        found = [time for time in self.tweets[tweetName] if startTime <= time <= endTime]
        found.sort(reverse=True)

        if freq  == 'minute':
            chunk = 60
        elif freq == 'hour':
            chunk = 3600
        else:
            chunk = 86400

        result = []
        time = startTime
        while time <= endTime:
            result.append(0)
            for i in range(chunk):
                while found and found[-1] == time + i:
                    result[-1] += 1
                    found.pop()
            time += chunk
        
        return result
        


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)
