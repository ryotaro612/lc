class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        n = len(row)

        person_pos = dict()
        for i in range(n):
            person_pos[row[i]] = i
        
        result = 0
        for i in range(0, n, 2):
            if row[i] // 2 == row[i+1] // 2:
                continue

            if row[i] // 2 * 2 == row[i]:
                other = row[i] + 1
            else:
                other = row[i] - 1
            
            result += 1
            other_i = person_pos[other]
            row[i+1], row[other_i] = row[other_i], row[i+1]
            person_pos[other] = i + 1
            person_pos[row[other_i]] = other_i

        return result
