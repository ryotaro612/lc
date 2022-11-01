"""
"internationalization"
"i12iz4n"

"apple"
"a2e"

"substitution"
"s10n"

"substitution"
"sub4u4"

"substitution"
"12"

"substitution"
"su3i1u2on"

"a"
"01"
"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(word)
        cursor = 0
        num = 0
        for c in abbr:
            if c.islower():
                cursor += num
                if n <= cursor or word[cursor] != c:
                    return False
                cursor += 1
                num = 0
            elif num == 0 and c == '0':
                return False
            else:
                num *= 10
                num += int(c)
        cursor += num
        return cursor == n
