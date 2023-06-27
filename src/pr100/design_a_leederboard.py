from collections import defaultdict
class Leaderboard:

    def __init__(self):
        self.players = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.players[playerId] += score        

    def top(self, K: int) -> int:
        return sum(sorted([score for score in self.players.values()], reverse=True)[:K])

    def reset(self, playerId: int) -> None:
        del self.players[playerId]


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
