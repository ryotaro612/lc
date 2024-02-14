class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos_list = []
        neg_list = []
        for num in nums:
            if num > 0:
                pos_list.append(num)
            else:
                neg_list.append(num)
        result = []
        
        for i in range(len(pos_list)):
            result.append(pos_list[i])
            result.append(neg_list[i])
        return result
