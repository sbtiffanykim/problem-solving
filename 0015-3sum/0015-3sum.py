class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        for i, val in enumerate(nums):
            if val > 0:  # bad case
                break
            if i > 0 and val == nums[i - 1]:  # ignore any duplicates
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                cur_sum = nums[left] + val + nums[right]
                if cur_sum > 0:
                    right -= 1
                elif cur_sum < 0:
                    left += 1
                else:
                    ans.append([val, nums[left], nums[right]])
                    left += 1  # move the pointer inward
                    right -= 1  # move the pointer inward
                    while nums[left] == nums[left - 1] and left <right:  # ignore any duplicates
                        left += 1
            
        return ans