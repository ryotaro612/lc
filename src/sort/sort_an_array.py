class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums))
        return nums
    
    def mergeSort(self, nums, start, end):
        if end <= start + 1:
            return
        
        mid = (start + end) // 2
        
        self.mergeSort(nums, start, mid)
        self.mergeSort(nums, mid, end)
        
        i = start
        j = mid
        temp = []
        while i < mid or j < end:
            if i < mid:
                if j < end:
                    if nums[i] <= nums[j]:
                        temp.append(nums[i])
                        i += 1
                    else:
                        temp.append(nums[j])
                        j += 1
                else:
                    temp.append(nums[i])
                    i += 1
            else:
                temp.append(nums[j])
                j += 1
        for i in range(start, end):
            nums[i] = temp[i-start]
