from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
        buckets=[[] for _ in range (len(nums)+1)]
        for num,count in freq.items():
            buckets[count].append(num)
        res = []
        for i in range(len(buckets) - 1, -1, -1):
            res.extend(buckets[i])
            if len(res) >= k:
                break
        return res[:k]