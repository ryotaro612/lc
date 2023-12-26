class Solution:
    def originalDigits(self, s: str) -> str:
        # 0 -> z, 2 -> w, 4 -> u, 6 -> x, 8 -> g
        #nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        # 1 -> o, 3 -> r, 5->f, 7 -> s
        #nums = ['one', 'three', 'five',  'seven',  'nine', 'ten']
        # 9-> i 10 -> t
        #nums = [ 'nine', 'ten']
        """
        for i in range(len(nums)):
                others = set()
                for j in range(len(nums)):
                    if i != j:
                        others = others | set(nums[j])
                
                print(nums[i], set(nums[i]) & others)
        """
        letters = [0] * 26
        for c in s:
            letters[ord(c) - ord('a')] += 1
        
        freq = [0] * 10
        for pattern in [[('z', 0, 'zero'), ('w', 2, 'two'), ('u', 4, 'four'), ('x', 6, 'six'), ('g', 8, 'eight')], \
                        [('o', 1, 'one'), ('r', 3, 'three'), ('f', 5, 'five'), ('s', 7, 'seven')], \
                        [('i', 9, 'nine')]]:
            for c, digit, text in pattern:
                freq[digit] = letters[ord(c) - ord('a')]
                for letter in text:
                    letters[ord(letter) - ord('a')] -= freq[digit]

        result = []
        for i, f in enumerate(freq):
            result.extend([str(i)] * f)
        return ''.join(result)
