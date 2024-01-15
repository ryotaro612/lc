from collections import defaultdict
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = defaultdict(lambda: [0, 0])
        for win, lose in matches:
            players[win][0] += 1
            players[lose][1] += 1
        answer = [[], []]
        for player, count in players.items():
            if count[0] and count[1] == 0:
                answer[0].append(player)
            if count[1] == 1:
                answer[1].append(player)
        answer[0].sort()
        answer[1].sort()
        return answer
