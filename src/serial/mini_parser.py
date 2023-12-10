# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

"""
s = [ SEQ | NUM
NUM = - POS | POS
POS = 0..9+
SEQ = ] | s (, s)* ]
"""
class Solution:
    def deserialize(self, s: str) -> NestedInteger:
        result = self.decode([c for c in s][::-1])
        # print(result)
        return self.transform(result)
    
    def transform(self, vals):
        if isinstance(vals, int):
            return NestedInteger(vals)
        else:
            res = NestedInteger()
            for v in vals:
                res.add(self.transform(v))
            return res

    def decode(self, stack):
        if stack[-1] == '[':
            stack.pop()
            return self.decode_seq(stack)
        else:
            return self.decode_num(stack)
    
    def decode_num(self, stack):
        sign = 1
        if stack[-1] == '-':
            sign = -1
            stack.pop()
        return sign * self.decode_pos(stack)
        
    def decode_pos(self, stack):
        res = 0
        while stack and stack[-1].isdigit():
            res = res * 10 + int(stack.pop())
            
        return res

    def decode_seq(self, stack):
        result = []

        while stack[-1] != ']':
            result.append(self.decode(stack))
            if stack[-1] == ',':
                stack.pop()
        stack.pop()
        return result
