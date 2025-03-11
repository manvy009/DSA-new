class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob_helper(start, end):
            prev1 = 0
            prev2 = 0
            for i in range(start, end + 1):
                current = max(prev1 + nums[i], prev2)
                prev1 = prev2
                prev2 = current
            return prev2

        case1 = rob_helper(0, len(nums) - 2)
        case2 = rob_helper(1, len(nums) - 1)

        return max(case1, case2)