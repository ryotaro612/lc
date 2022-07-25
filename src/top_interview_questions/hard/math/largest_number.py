
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result_index = [0]
        for i in range(1, len(nums)):
            running_index = result_index + [i]
            running_str = ''.join([str(nums[j]) for j in running_index])
            for j in range(len(result_index)):
                temp_index = result_index[:j] + [i] + result_index[j:]
                temp_str = ''.join([str(nums[k]) for k in temp_index])
                if running_str < temp_str:
                    running_str = temp_str
                    running_index = temp_index
            result_index = running_index
        result = ''.join([str(nums[i]) for i in result_index]) 
        if set(result) == {'0'}:
            return '0'
        else:
            return result
