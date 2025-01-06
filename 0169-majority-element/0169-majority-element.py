class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        cnt=0
        ele=None
        for i in range(n):
            if cnt==0:
                cnt=1
                ele=nums[i]
            elif ele == nums[i]:
                cnt += 1
            else:
                cnt -= 1
        return ele
        