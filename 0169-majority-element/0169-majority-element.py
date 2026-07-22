class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ca=None
        c=0
        for i in nums:
            if c==0:
                ca=i
            if ca==i:
                c+=1
            else:
                c-=1
        return ca

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna