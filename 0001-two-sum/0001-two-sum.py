class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_table = {val: idx for idx, val in enumerate(nums)}

        for idx, val in enumerate(nums):
            if target - val in num_table and idx != num_table[target-val]:
                return [idx, num_table[target- val]]
