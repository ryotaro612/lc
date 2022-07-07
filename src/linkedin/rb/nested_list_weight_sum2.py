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

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        max_depth = 0
        for child in nestedList:
            max_depth = max(max_depth, self.findMaxDepth(child, 1))
        result = 0
        for child in nestedList:
            result += self.computeWeightedInt(child, max_depth, 1)
        return result
        
    def findMaxDepth(self, nestedList, depth):
        if nestedList.isInteger():
            return depth
        result = 0
        for child in nestedList.getList():
            result = max(result, self.findMaxDepth(child, depth+1))
        return result
    
    def computeWeightedInt(self, nestedList, max_depth, depth):
        if nestedList.isInteger():
            # maxDepth - (the depth of the integer) + 1.
            return nestedList.getInteger() * (max_depth - depth + 1)
        
        result = 0
        for child in nestedList.getList():
            result += self.computeWeightedInt(child, max_depth, depth+1)
        return result
