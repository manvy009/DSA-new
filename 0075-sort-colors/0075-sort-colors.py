class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low=0
        mid=0
        high=0
        for i in nums:
            if i==0:
                low+=1
            elif i==1:
                mid+=1
            else:
                high+=1
        for i in range(len(nums)):
            if low>0:
                nums[i]=0
                low-=1
            elif mid>0:
                nums[i]=1
                mid-=1
            else:
                nums[i]=2
                high-=1

        