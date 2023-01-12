class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        largest = max(damage)
        total = sum(damage) - largest
        return total + 1 + max(0, largest - armor)
