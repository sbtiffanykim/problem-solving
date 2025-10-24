class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_max = res = nums[0]

        for i in range(1, len(nums)):
            cur_max = max(cur_max + nums[i], nums[i])  # Extend the previous subarray or start at the new position
            res = max(res, cur_max)  # Update the maximum sum

        return res