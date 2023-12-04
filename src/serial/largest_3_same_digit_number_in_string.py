class Solution:
    def largestGoodInteger(self, num: str) -> str:
        patterns = []
        for i in range(10):
            patterns.append(str(i) * 3)
        
        result = ''
        for pattern in patterns:
            for i in range(len(num)-2):
                if pattern == num[i:i+3]:
                    result = pattern
        return result
