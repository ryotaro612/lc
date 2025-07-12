class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        result = 0
        players.sort()
        trainers.sort()
        i_p = i_t =0
        
        n_t = len(trainers)
        n_p = len(players)

        while i_p < n_p and i_t < n_t:
            if players[i_p] <= trainers[i_t]:
                result += 1
                i_p += 1
                i_t += 1
                continue
            i_t += 1
        
        return result
