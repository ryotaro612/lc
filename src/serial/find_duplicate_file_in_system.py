from collections import defaultdict
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        found = defaultdict(list)
        for path in paths:
            items = path.split(' ')
            directory = items[0]
            for name_content in items[1:]:
                mid = name_content.find('(')
                found[name_content[mid:]].append(f"{directory}/{name_content[:mid]}")
        
        return [v for v in found.values() if len(v) > 1]
