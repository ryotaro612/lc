from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False
        
        hand.sort()
        freq = defaultdict(int)
        total = 0
        for i, e in enumerate(hand):
            if total > n - i:
                return False
            if freq[e]:
                freq[e] -= 1
                total -= 1
            else:
                for a in range(e+1, e+groupSize):
                    freq[a] += 1
                    total += 1
        for v in freq.values():
            if v:
                return False
        return True
