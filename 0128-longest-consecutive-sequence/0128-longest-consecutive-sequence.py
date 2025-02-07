class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        l=1
        st=set()
        for i in range(n):
            st.add(nums[i])
        for it in st:
            if it-1 not in st:
                cnt=1
                x=it
                while x+1 in st:
                    x+=1
                    cnt+=1
                l=max(cnt,l)
        return l