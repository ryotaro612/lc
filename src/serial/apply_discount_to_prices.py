class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        lst = []
        n = len(sentence)
        i = 0
        digits = {str(i) for i in range(10)}
        while i < n:
            if not (sentence[i] == '$' and (i == 0 or sentence[i-1] == ' ')):
                lst.append(sentence[i])
                i += 1
                continue
            
            lst.append(sentence[i])
            i += 1
            temp = []
            ok = True
            while i < n:
                if sentence[i] in digits:
                    temp.append(sentence[i])
                    i += 1
                else:
                    break
            
            if len(temp) and (i == n or sentence[i] == ' '):
                price = int(''.join(temp))
                price -= price * discount/100
                lst.append(f'{price:.2f}')
            else:
                lst.extend(temp)

        return ''.join(lst)
