"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""
from collections import defaultdict

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        n = len(employees)
        id_idx = dict()
        for i, employee in enumerate(employees):
            id_idx[employee.id] = i
        
        cache = defaultdict(int)

        return self.solve(id, employees, id_idx, cache)
    
    def solve(self, id, employees, id_idx, cache):
        if id in cache:
            return cache[id]
        
        employee = employees[id_idx[id]]
        result = employee.importance
        for child in employee.subordinates:
            result += self.solve(child, employees, id_idx, cache)
        
        cache[id] = result
        return result
