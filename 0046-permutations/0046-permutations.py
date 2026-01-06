class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index, path):
            # Base case
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                # Constraint: cannot reuse the sanme number more than once in the path
                if nums[i] in path:
                    continue
                
                path.append(nums[i])
                backtrack(index + 1, path)
                path.pop()  # backtracking step

        backtrack(0, [])
        return result