class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i + 1 for i in range(n)]
        pos = 0
        while len(players) > 1:
            remove_pos = (pos + (k-1)) % len(players)
            players = players[:remove_pos] + players[remove_pos+1:]
            pos = (remove_pos) % len(players)
        
        return players[0]
