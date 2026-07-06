class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left=1
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            c=0
            for num in nums:
                if num<=mid:
                    c+=1
            if c>mid:
                right=mid
            else:
                left=mid+1
        return left


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna