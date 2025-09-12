class Solution:
    def doesAliceWin(self, s: str) -> bool:
        """
        n = #of vowels
        alice, bob[0..n+1] x
        alice[i] = True win i
        bob[i] = True i

        alice[i] = True iff bob[i-(2*j+1)] = False exists bob_even_false bob[k], bob_odd_false 
        bob[i] = Trre iff alice[i-(2*(j+1))] = False exists
        return alice[n]
        """
        n = 0
        for c in s:
            if c in 'aeiou':
                n+=1
        if n == 0:
            return False
        
        alice = [False] * (n+1)
        bob = [False] * (n+1)

        bob_even_f = bob_odd_f = False
        alice_even_f = alice_odd_f = False

        if n % 2:
            return True

        for i in range(1, n+1):
            if i % 2:
                if bob_even_f:
                    alice[i] = True
                if alice_even_f:
                    bob[i] = True
                
                if not alice[i]:
                    alice_odd_f = True
                if not bob[i]:
                    bob_odd_f = True
            else:
                if bob_odd_f:
                    alice[i] = True
                if alice_even_f:
                    bob[i] = True
            
                if not alice[i]:
                    alice_even_f = True
                if not bob[i]:
                    alice_even_f = True
        
        return alice[n]
            
