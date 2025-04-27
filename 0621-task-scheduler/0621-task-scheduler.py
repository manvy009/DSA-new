class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=collections.Counter(tasks)
        maxx=max(freq.values())
        freq=list(freq.values())
        max_freq_ele_cnt=0
        i=0
        while(i<len(freq)):
            if freq[i]==maxx:
                max_freq_ele_cnt+=1
            i+=1
        ans=(maxx-1)*(n+1)+max_freq_ele_cnt
        return max(ans,len(tasks))