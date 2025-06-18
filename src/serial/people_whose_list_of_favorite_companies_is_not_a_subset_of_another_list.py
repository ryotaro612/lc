class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        companies = [set(cs) for cs in favoriteCompanies]
        result = []
        n = len(companies)
        
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                if len([c for c in companies[i] if c in companies[j]]) == len(companies[i]):
                    break
            else:
                result.append(i)
        return result
