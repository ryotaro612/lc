"""
"DDRRR"
"""


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        counter = 0

        while True:
            if len(set(senate)) == 1:
                if senate[0] == "R":
                    return "Radiant"
                else:
                    return "Dire"

            enable = [True for _ in range(len(senate))]
            for i, senator in enumerate(senate):
                if senator == "R":
                    if counter < 0:
                        enable[i] = False
                    counter += 1
                else:
                    if counter > 0:
                        enable[i] = False
                    counter -= 1
            senate = [s for s, e in zip(senate, enable) if e]
