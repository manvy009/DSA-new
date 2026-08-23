class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max = curr_min = result = nums[0]
        for i in range(1,len(nums)):
            prev_max=curr_max
            prev_min=curr_min

            curr_max=max(nums[i],prev_max*nums[i],prev_min*nums[i])
            curr_min=min(nums[i],prev_max*nums[i],prev_min*nums[i])
            result=max(result,curr_max)
        return result


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna