class Solution:
    def average(self, salary: List[int]) -> float:
        min_salary = min(salary)
        max_salary = max(salary)
        result = 0
        for s in salary:
            if s not in {min_salary, max_salary}:
                result += s

        return result / (len(salary) - 2)
