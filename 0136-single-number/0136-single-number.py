class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq={}
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
        for key in freq:
            if freq[key]==1:
                return key