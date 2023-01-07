"""
[3,4,8,9,3,0]
[6,1,9,1,1,2]
6

[2]
[2,9,7,7,9,2,5,5,1,9,6,8,4,5,1,3,3,1,4,8,7,1,8,2,2,9,6,9,9,7,4,0,6,5,9,0,4,7,6,8,0,1,6]
44

[3,3,3,2,3,7,3,8,6,0,5,0,7,8,9,2,9,6,6,9,9,7,9,7,6,1,7,2,7,5,5,1]
[5,6,4,9,6,9,2,2,7,5,4,3,0,0,1,7,1,8,1,5,2,5,7,0,4,3,8,7,3,8,5,3,8,3,4,0,2,3,8,2,7,1,2,3,8,7,6,7,1,1,3,9,0,5,2,8,2,8,7,5,0,8,0,7,2,8,5,6,5,9,5,1,5,2,6,2,4,9,9,7,6,5,7,9,2,8,8,3,5,9,5,1,8,8,4,6,6,3,8,4,6,6,1,3,4,1,6,7,0,8,0,3,3,1,8,2,2,4,5,7,3,7,7,4,3,7,3,0,7,3,0,9,7,6,0,3,0,3,1,5,1,4,5,2,7,6,2,4,2,9,5,5,9,8,4,2,3,6,1,9]
160
"""
class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        result = None
        for i in range(0, k+1):
            sub1 = self.select(nums1, i)
            sub2 = self.select(nums2, k-i)
            # print(sub1, sub2)
            if len(sub1) != i or len(sub2) != k - i:
                continue
            a = 0
            b = 0
            temp = []
            while len(temp) < k:
                peek = 0
                while a + peek < i and b + peek < k-i and sub1[a+peek] == sub2[b+peek]:
                    peek += 1
                if a + peek == i or b + peek == k-i:
                    if a + peek == i:
                        temp.append(sub2[b])
                        b += 1
                    else:
                        temp.append(sub1[a])
                        a += 1
                else:
                    if sub1[a+peek] < sub2[b+peek]:
                        temp.append(sub2[b])
                        b += 1
                    else:
                        temp.append(sub1[a])
                        a += 1
            # print(sub1, sub2, temp)
            if result:
                result = max(temp, result)
            else:
                result = temp
        return result

    def select(self, nums, n_select):
        n = len(nums)
        stack = []
        for i, num in enumerate(nums):
            if stack:
                if stack[-1] >= num:
                    stack.append(num)
                else:
                    while stack and len(stack) + n - i > n_select and stack[-1] < num:
                        stack.pop()
                    stack.append(num)
            else:
                stack.append(num) 
        return stack[:n_select]
