from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        
        for i, group_size in enumerate(groupSizes):
            d[group_size].append(i)
        
        result = []
        for group_size, people in d.items():
            while people:
                element = []
                for _ in range(group_size):
                    element.append(people.pop())
                result.append(element)
        return result
