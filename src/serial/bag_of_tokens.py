import heapq
class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        score = 0
        result = score
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                result = max(result, score)
            elif score:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return result
