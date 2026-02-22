from collections import Counter as C
from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f=C(nums)
        hp=[]
        for i in f:
            heappush(hp,(-f[i],i))
        r=[]
        for _ in range(k):
            r.append(heappop(hp)[1])
        return r