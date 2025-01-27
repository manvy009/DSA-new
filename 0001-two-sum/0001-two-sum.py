class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nwi=[(num,i)for i,num in enumerate(nums)]
        nwi.sort(key=lambda x:x[0])
        l,r=0,len(nums)-1
        while l<r:
            s=nwi[l][0]+nwi[r][0]
            if s==target:
                return [nwi[l][1], nwi[r][1]]
            elif s<target:
                l+=1
            else:
                r-=1
        return []