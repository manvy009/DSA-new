from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l=[]
        n=len(nums)
        c=Counter(nums)
        for num, cnt in c.items():
            if cnt > (n // 3):
                l.append(num)
        return l