class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(price)
        
        special = [s for s in special if [num for num in s[:-1] if num]]
        cache = dict()
        return self.find_lowest(price, special, needs, cache)

    def find_lowest(self, price, special, needs, cache):
        if tuple(needs) in cache:
            return cache[tuple(needs)]

        if [] == [need for need in needs if need]:
            cache[tuple(needs)] = 0
            return 0
        
        result = 0
        for i, need in enumerate(needs):
            result += need * price[i]
        
        n = len(needs)
        for s in special:
            ok = True
            for i in range(n): 
                if needs[i] < s[i]:
                    ok = False
            if ok:
                for i in range(n):
                    needs[i] -= s[i]
                result = min(result, s[-1] + self.find_lowest(price, special, needs, cache))
                for i in range(n):
                    needs[i] += s[i]
        
        cache[tuple(needs)] = result
        return result
