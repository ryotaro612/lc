class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {i: v for i, v in enumerate(nums) if v != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        
        result = 0
        
        for i in self.nums:
            result += self.nums[i] * vec.nums.get(i, 0)
            
        return result
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
