gclass Solution:
    def bestClosingTime(self, customers: str) -> int:
      n_y = customers.count('Y')
      n = len(customers)
      min_penalty = penalty = n_y
      result = 0

      for i in range(1, n+1):
        if customers[i-1] == 'Y':
          penalty -= 1
        else:
          penalty += 1
        if penalty < min_penalty:
          result = i
          min_penalty = penalty
      return result

