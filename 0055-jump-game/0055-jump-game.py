class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fuel=0
        for n in nums:
            if fuel<0:
                return False
            elif fuel<n:
                fuel=n
            fuel-=1
        return True