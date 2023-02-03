class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        result = []
        n1, n2, n3 = [len(a) for a in [arr1, arr2, arr3]]
        i = [0, 0, 0]

        while i[0] < n1 and i[1] < n2 and i[2] < n3:
            if arr1[i[0]] == arr2[i[1]] == arr3[i[2]]:
                result.append(arr1[i[0]])
                i[0] += 1
                i[1] += 1
                i[2] += 1
            else:
                idx = sorted([[arr1[i[0]], 0], [arr2[i[1]], 1], [arr3[i[2]], 2]])[0][1]
                
                i[idx] += 1
        
        return result
