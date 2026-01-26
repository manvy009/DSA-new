class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum=0
        seen={0:1}
        c=0
        for x in nums:
            curr_sum+=x
            need=curr_sum-k
            if need in seen:
                c+=seen[need]

            if curr_sum in seen:
                seen[curr_sum]+=1
            else:
                seen[curr_sum]=1
        return c
