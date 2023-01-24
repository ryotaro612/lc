import bisect
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = bisect.bisect_right([ord(c) for c in letters], ord(target))
        if len(letters) == i:
            return letters[0]
        else:
            return letters[i]
