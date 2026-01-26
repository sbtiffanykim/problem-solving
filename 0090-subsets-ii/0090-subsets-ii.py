class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(index, path):
            # base case
            if len(nums) == index:
                result.append(path[:])
                return
            
            # 1. Include nums[index]
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()  # backtracking step

            # constraints: skip all consecutive duplicates of the current number
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            # 2. Exclude nums[index]
            backtrack(index + 1, path)

        backtrack(0, [])
        return result
