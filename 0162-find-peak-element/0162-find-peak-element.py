class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        ans=0
        while l<r:
            m=(l+r)//2
            if nums[m]<nums[m+1]:
                l=m+1
            elif nums[m]<nums[m-1]:
                r=m-1
            else:
                return m
        return l
