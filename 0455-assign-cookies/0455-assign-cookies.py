class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l=0
        g.sort()
        s.sort()
        for coo in s:
            if coo >= g[l]:
                l+=1
                if l==len(g):
                    break
        return l