from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        deck.sort()
        result = [0] * n
        cur = 0
        order = deque(list(range(n)))

        while order:
            top = order.popleft()
            result[top] = deck[cur]
            cur += 1
            if order:
                top = order.popleft()
                order.append(top)
        
        return result
