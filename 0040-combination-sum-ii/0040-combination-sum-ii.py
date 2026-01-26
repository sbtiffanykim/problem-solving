class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(index, path):
            print(index, path)
            # base case: sum >= target or index == len(candidates)
            if sum(path) >= target or index == len(candidates):
                # add to the result when the sum of current path is equal to the target
                if sum(path) == target:
                    result.append(path[:])
                return

            # include nums[index]
            path.append(candidates[index])
            backtrack(index + 1, path)
            path.pop()

            # skip all consecutive duplicates
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            # exclude nums[index]
            backtrack(index + 1, path)
        
        backtrack(0, [])
        return result