from collections import defaultdict

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        id_scores = defaultdict(list)

        for student, score in items:
            id_scores[student].append(score)

        result = []
        for student in sorted(id_scores.keys()):
            scores = sorted(id_scores[student], reverse=True)
            result.append([student, sum(scores[:5]) // 5])

        return result
