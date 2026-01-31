class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d={0:-1}
        curr_sum=0
        for i in range(len(nums)):
            curr_sum+=nums[i]
            if k!=0:
                curr_sum%=k
            if curr_sum in d:
                if i - d[curr_sum]>=2:
                    return True
            else:
                d[curr_sum]=i
        return False