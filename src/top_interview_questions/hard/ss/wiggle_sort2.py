import random
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        def nsmallest(nums,n):            
            start,end=0,len(nums)-1
            while True:
                pivot=nums[random.randint(start,end)]
                i,j,k=start,end,start
                while k<=j:
                    if nums[k]<pivot:
                        nums[i],nums[k]=nums[k],nums[i]
                        i+=1
                        k+=1
                    elif nums[k]>pivot:
                        nums[j],nums[k]=nums[k],nums[j]
                        j-=1
                    else:
                        k+=1
                if i<=n-1<=j:
                    return pivot
                elif n-1<i:
                    end=i-1
                else:
                    start=j+1
        n=len(nums)
        mid=nsmallest(nums,(n+1)//2)
        mapIdx=lambda i:(1+2*i)%(n|1)
        i,j,k=0,n-1,0
        while k<=j:
            if nums[mapIdx(k)]>mid:
                nums[mapIdx(k)],nums[mapIdx(i)]=nums[mapIdx(i)],nums[mapIdx(k)]
                i+=1
                k+=1
            elif nums[mapIdx(k)]<mid:
                nums[mapIdx(k)],nums[mapIdx(j)]=nums[mapIdx(j)],nums[mapIdx(k)]
                j-=1
            else:
                k+=1
"""
    def find_kth(self, nums, index):
        start, end = 0, len(nums) - 1
        while True:
            i, j, mid = start, end, start
            pivot = nums[random.randrange(start, end+1)]
            while mid <= j:
                if nums[mid] < pivot:
                    nums[i], nums[mid] = nums[mid], nums[i]
                    i += 1
                    mid += 1
                elif pivot < nums[mid]:
                    nums[j-1], nums[mid] = nums[mid], nums[j-1]
                    j -= 1
                else:
                    mid += 1
            if i <= index <= j:
                return pivot
            elif index < i:
                end = i - 1
            else:
                start = i + 1
                    
"""
