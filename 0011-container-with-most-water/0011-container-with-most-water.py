class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        res=0
        while i<j:
            res=max(res,(j-i)*min(height[i],height[j]))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna