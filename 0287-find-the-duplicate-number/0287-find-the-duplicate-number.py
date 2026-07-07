class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=nums[0]
        f=nums[0]
        while True:
            s=nums[s]
            f=nums[nums[f]]
            if s==f:
                break
        s=nums[0]
        while s!=f:
            s=nums[s]
            f=nums[f]
        return s


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna